from django.apps import AppConfig


class AppProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_projects'

    def ready(self):
        from . import cron
        cron.start()