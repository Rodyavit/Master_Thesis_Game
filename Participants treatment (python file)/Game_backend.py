from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'bandwagon_game'
    PLAYERS_PER_GROUP = 100
    NUM_ROUNDS = 1
    BASELINE="baseline"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        label='What is your age ? / Quel âge avez-vous?', min=13, max=123)
    gender = models.StringField(
        choices=[[1, 'Male'],
                 [2, 'Female'],
                 [3, 'Other']],
        label='What is your gender? / Quel est votre genre ?',
        widget=widgets.RadioSelectHorizontal)
    student = models.IntegerField(
        choices=[[1, 'Yes'],
                 [2, 'No']],
                 label='Are you a student? / Etes vous un(e) étudiant(e) ?',
        widget=widgets.RadioSelectHorizontal)
    wine = models.IntegerField(
        choices=[[1, '1'],
                 [2, '2'],
                 [3, '3'],
                 [4, '4'],
                 [5, '5'],
                 [6, '6'],
                 [7, '7'],
                 [8, '8'],
                 [9, '9'],
                 [10, '10']],
        label='One a scale of 1 to 10 how much do you like Bordeaux wine? / Sur une échelle de 1 à 10, à quel point appréciez-vous le Bordeaux? (1=👎 10=😍)',
        widget=widgets.RadioSelectHorizontal)
    wine_knowledge = models.IntegerField(
        choices=[[1, '1'],
                 [2, '2'],
                 [3, '3'],
                 [4, '4'],
                 [5, '5'],
                 [6, '6'],
                 [7, '7'],
                 [8, '8'],
                 [9, '9'],
                 [10, '10']],
        label='On a scale of 1 to 10, how would you rate your wine knowledge?  / Sur une échelle de 1 à 10, à combien évaluez vous votre connaissance en vin ?(1=👎 10=💪)',
        widget=widgets.RadioSelectHorizontal)
    choose_wine = models.IntegerField(
        choices=[[1, ' The bottle of wine / La bouteille de vin '],
                 [2, '10€ discount / 10 € de réduction']],
        label='What do you choose ? / Que choisissez vous ?',
        widget=widgets.RadioSelectHorizontal)
    wine_availability = models.IntegerField(
        choices=[[0, '0%'],
                 [10, '10%'],
                 [20, '20%'],
                 [30, '30%'],
                 [40, '40%'],
                 [50, '50%'],
                 [60, '60%'],
                 [70, '70%'],
                 [80, '80%'],
                 [90, '90%'],
                 [100, '100%']],
        label='A stock of this bottle of wine has been built up for this offer. In your opinion, what percentage of bottles (of the stock) has already been offered to customers? <br><br>Un stock de cette bouteille de vin a été constitué pour cette offre. A votre avis, quel pourcentage de bouteilles (du stock) a déjà été offert aux clients ? <br><br> ',
        widget=widgets.RadioSelectHorizontal)
    accept_price = models.FloatField(
        choices=[[11, '11€'],
                 [12, '12€'],
                 [13, '13€'],
                 [14, '14€'],
                 [16, '16€'],
                 [18, '18€'],
                 [20, '20€'],
                 [25, '25€'],
                 [30, '30€'],
                 [40, '40€'],
                 [50, '>50€']],
        label='You chose the bottle of wine instead of the discount. However, if the shop had offered a bigger discount (more than €10). At what discount level would you have changed your mind and chosen the discount? <br><br> Vous avez choisi la bouteille de vin au lieu de la réduction. Cependant, si le magasin avait proposé une réduction plus importante (plus de 10€). A partir de quel montant de réduction auriez vous changé d avis et choisi la réduction ?<br><br>',
        widget=widgets.RadioSelectHorizontal)
    refuse_price = models.IntegerField(
        choices=[[0, '0€'],
                 [1, '1€'],
                 [2, '2€'],
                 [3, '3€'],
                 [4, '4€'],
                 [5, '5€'],
                 [6, '6€'],
                 [7, '7€'],
                 [8, '8€'],
                 [9, '9€']],
        label='You chose the discount instead of the bottle of wine. However, if the shop had offered a smaller discount (less than €10). At what point would you have changed your mind and chosen the bottle of wine? <br><br> Vous avez choisi la réduction au lieu de la bouteille de vin. Cependant, si le magasin avait proposé une réduction moins importante (moins de 10 €). A partir de quel montant de réduction auriez vous changé d avis et choisi la bouteille de vin?  <br><br>',
        widget=widgets.RadioSelectHorizontal)





# METHODS ==============================================================================================================

#TO RANDOMISE PARTICIPANTS
def creating_session(subsession):
    subsession.group_randomly()

# PAGES
class Welcoming_page(Page):
    pass

class Scenario(Page):
    pass

class Choice(Page):
    form_model = "player"
    form_fields = ["choose_wine"]
    pass

class Demographics(Page):
    form_model="player"
    form_fields=["age","student","gender","wine_knowledge","wine"]
    pass

class Explaining_page(Page):
    pass

class Control_groupe_wine_choice(Page):
    def is_displayed(player: Player):
        return player.group.id_in_subsession== 3
    pass

class Test_groupe_wine_choice(Page):
    def is_displayed(player: Player):
        return player.group.id_in_subsession in [1,2]
    pass

class Refuse_stock(Page):
    def is_displayed(player: Player):
        return player.group.id_in_subsession in [1,3] and player.choose_wine == 2
    pass

class Accept_stock(Page):
    def is_displayed(player: Player):
        return player.group.id_in_subsession in [1,3] and player.choose_wine == 1
    pass

class Availability_wine_page(Page):
    form_model="player"
    form_fields=["wine_availability"]
    pass

class Refuse_wine_price_page(Page):
    form_model="player"
    form_fields=["refuse_price"]
    def is_displayed(player: Player):
        return player.choose_wine==2
    pass

class Accept_wine_page(Page):
    form_model="player"
    form_fields=["accept_price"]
    def is_displayed(player: Player):
        return player.choose_wine==1
    pass




page_sequence = [Welcoming_page, Scenario,Control_groupe_wine_choice,Test_groupe_wine_choice,Choice,Refuse_stock,Accept_stock,Availability_wine_page,Refuse_wine_price_page,Accept_wine_page,Demographics,Explaining_page]
