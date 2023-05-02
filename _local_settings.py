# Пример local_settings
# Измените данные на свои

DEBUG = True
ALLOWED_HOSTS = ['*', 'b8d8-46-252-249-158.ngrok-free.app', "0.0.0.0"]

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

APP_SETTINGS = LocalSettingsClass(
    portal_domain='kad-1.bitrix24.ru',
    app_domain='127.0.0.1:8000',
    app_name='is-demo',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.644b9111ab2591.39587044',
    application_bitrix_client_secret='secret',
    application_index_path='/',
)



DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'is_demo',  # Or path to database file if using sqlite3.
    #     'USER': 'postgres',  # Not used with sqlite3.
    #     'PASSWORD': '123qweASD',  # Not used with sqlite3.
    #     'HOST': 'localhost',
    # },
    "default": {
        "NAME": "ru_sites",
        'OPTIONS': {
            'options': '-c search_path=ru_sites_info'
        },
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "USER": "postgres",
        "PASSWORD": "123qweASD",
        'HOST': 'localhost',
    },
}