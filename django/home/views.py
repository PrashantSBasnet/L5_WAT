import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

'''Class-Based Views'''


class HomeView(TemplateView):
    template_name = "home/welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.date.today()
        return context


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"
