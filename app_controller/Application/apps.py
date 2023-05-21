from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Application'


    'For Signal'
    # def ready(self):
    #     import Application.signal
