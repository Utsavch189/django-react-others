from django.apps import AppConfig


class DjangoSignalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_signal_app'

    def ready(self):
        import django_signal_app.signal
