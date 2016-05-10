from django.contrib.sites import shortcuts


def common(request):
    # try:
    #     theme = request.host.theme
    # except:
    #     theme = 'default'
    print(repr(request.get_host()))
    print(shortcuts.get_current_site(request))
    return {
    }
