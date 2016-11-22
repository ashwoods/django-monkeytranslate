from django.utils.safestring import SafeData, mark_safe
from django.utils.translation import trans_real

_do_translate = trans_real.do_translate


def wrap_translate(*args, **kwargs):
    translation_string = _do_translate(*args, **kwargs)
    return mark_safe('{%s}' % translation_string)
