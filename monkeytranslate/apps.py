
from django.apps import AppConfig
from django.utils.translation import trans_real

from .conf import settings


class MonkeyTranslateAppConfig(AppConfig):

    name = 'monkeytranslate'
    verbose_name = 'Monkey translate'

    def ready(self):
        if settings.MONKEYTRANSLATE_ENABLED:
            trans_real.do_translate = settings.MONKEYTRANSLATE_CALLABLE

