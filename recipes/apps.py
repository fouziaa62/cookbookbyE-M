from django.apps import AppConfig

class CookbookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    def ready(self):
        import recipes.signals
