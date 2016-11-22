from django.conf import settings  # noqa

from appconf import AppConf
from .utils import wrap_translate


class MonkeyTranslateConf(AppConf):
    ENABLED = False
    CALLABLE = wrap_translate
