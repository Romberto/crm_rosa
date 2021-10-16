from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View

from butler.forms import AuthForm

""" выход пользователя из системы """

class LogOut(LogoutView) :
    template_name = "butler/auth.html"

""" авторизация пользователя в системе """


class AuthenticationView(LoginView):
    template_name = 'butler/auth.html'
    form_class = AuthForm


""" определение роли пользователя"""


class RoleUser(View):
    def get(self, request):
        if request.user.groups.filter(name='manager').exists():
            return redirect('/manager')
        elif request.user.groups.filter(name='boss').exists():
            data = {'data': request.user}
            return render(request, 'butler/test.html', data)
        else:
            return redirect('/')

""" декоратор проверяющий авторизацию пользователя"""

def auth_decoration(func):
    def wraper(self, request):
        if not request.user.is_authenticated:
            return redirect('/')
        return func(self, request)
    return wraper



