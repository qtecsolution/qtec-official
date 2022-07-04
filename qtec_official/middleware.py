from django.http import HttpResponseRedirect
from django.urls import resolve


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        current_url = resolve(request.path_info).url_name
        get_full_path = request.get_full_path().split('/')
        if 'dashboard' in get_full_path:
            if not request.user.is_authenticated:
                if current_url != 'dashboard_login_url':
                    return HttpResponseRedirect('/dashboard/login/')
            else:
                return self.get_response(request)

        return self.get_response(request)
