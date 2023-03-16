from django import conf
from django.apps import AppConfig, apps
from django.utils.functional import SimpleLazyObject, empty


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def __getattr__(self, name):
        return getattr(conf.settings, name, None) or getattr(self, name)


settings = SimpleLazyObject(lambda: apps.app_configs.get(CoreConfig.name) or empty)
