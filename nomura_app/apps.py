from django.apps import AppConfig


class NomuraAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nomura_app'

    def ready(self):
    	import nomura_app.signals
