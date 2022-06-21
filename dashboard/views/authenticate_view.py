from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class AuthenticationView(View):

    def get(self, request):
        if request.resolver_match.url_name == 'dashboard_login_url':
            return render(request, 'login.html', {'page_title': 'Login'})

        if request.resolver_match.url_name == 'logout_dashboard_url':
            auth.logout(request)
            return redirect('dashboard:dashboard_login_url')

    def post(self, request):

        if request.resolver_match.url_name == 'dashboard_login_url':
            username = request.POST['username'].strip()
            password = request.POST['password'].strip()

            try:
                user_obj = User.objects.get(username=username)
            except Exception as e:
                return render(request, 'login.html',
                              {'error': 'This Username doesn\'t exist, please input your valid Username'})

            if user_obj.check_password(password):
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('dashboard:dashboard_url')
            else:
                return render(request, 'login.html', {'error': 'Password doesn\'t match '})