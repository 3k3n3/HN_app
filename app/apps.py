from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    # # APScheduler config
    def ready(self):
        from schedule import updater
        updater.start()
