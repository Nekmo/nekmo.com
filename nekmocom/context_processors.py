from django.conf import settings
from django.contrib.sites import shortcuts


def common(request):
    # try:
    #     theme = request.host.theme
    # except:
    #     theme = 'default'
    return {
        'nekmocom_static_dir': 'nekmocom/{}/'.format('src' if getattr(settings, 'BOOTSTRAP3_FORCE_SRC',
                                                                      False) else 'dist')
    }
