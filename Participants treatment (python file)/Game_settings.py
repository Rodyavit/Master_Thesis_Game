from os import environ

SESSION_CONFIGS = [
    dict(
         name='bandwagon_game',
         display_name="Bandwagon game",
         app_sequence=['bandwagon_game'],
         num_demo_participants=300,
        treatment="baseline"
     ),
]

ROOMS = [
    dict(
        name="Thesis_game_room",
        display_name="Thesis_game",
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


