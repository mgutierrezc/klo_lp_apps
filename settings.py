from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'MoneyPolitics',
        'num_demo_participants': 9,
        'app_sequence': ['MoneyPolitics'],
        # Display player ID
        'show_id': True,
        # Display player income
        'show_income': True,
        # Which game will be played (Tetris or Diamonds)
        'treatment': "Tetris",
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "tax_rate",
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
POINTS_DECIMAL_PLACES = 1
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '^sj1@)7g$9!w19h=jyd0sdqof@uwo2f^_d-zy9ra!rg!rf!ku*'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
