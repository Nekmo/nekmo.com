from cms.utils.conf import _ensure_languages_settings, VERIFIED, COMPLEX
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import cms.utils.conf
from django.utils.translation import ugettext_lazy as _



def get_languages():
    if settings.SITE_ID != hash(settings.SITE_ID):
        # TODO: esto es una prueba
        pass
        # raise ImproperlyConfigured(
        #     "SITE_ID must be an integer"
        # )
    if not settings.USE_I18N:
        return _ensure_languages_settings(
            # TODO:
            {int(settings.SITE_ID): [{'code': settings.LANGUAGE_CODE, 'name': settings.LANGUAGE_CODE}]})
    if settings.LANGUAGE_CODE not in dict(settings.LANGUAGES):
        raise ImproperlyConfigured(
            'LANGUAGE_CODE "%s" must have a matching entry in LANGUAGES' % settings.LANGUAGE_CODE
        )
    # TODO:
    languages = getattr(settings, 'CMS_LANGUAGES', {
        int(settings.SITE_ID): [{'code': code, 'name': _(name)} for code, name in settings.LANGUAGES]
    })
    if VERIFIED in languages:
        return languages
    return _ensure_languages_settings(languages)

setattr(cms.utils.conf, 'get_languages', get_languages)

COMPLEX['LANGUAGES'] = get_languages
