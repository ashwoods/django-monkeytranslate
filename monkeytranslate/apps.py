class MonkeyTranslateAppConfig(AppConfig):

    name = 'monkeytranslate'
    verbose_name = 'Monkey translate'

    def ready(self):
        from django.utils.translation import trans_real
        from django.utils.safestring import SafeData, mark_safe

        _do_translate = trans_real.do_translate

        def do_translate(*args, **kwargs):
             translation_string = _do_translate(*args, **kwargs)
            return mark_safe('{%s}' % translation_string)

        trans_real.do_translate = do_translate

