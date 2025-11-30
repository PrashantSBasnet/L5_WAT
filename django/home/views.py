import datetime

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import TemplateView

'''Class-Based Views'''

class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

class LogoutInterfaceView(LogoutView):
    #Subclass LogoutView and override post()
    #more secure way
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("home/login.html")  # or wherever you want

class HomeView(TemplateView):
    template_name = "home/welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.date.today()
        return context


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"
