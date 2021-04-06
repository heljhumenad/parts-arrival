from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class MessageMixin(LoginRequiredMixin, SuccessMessageMixin):
    login_url = reverse_lazy("login")
    redirect_field_name = "next_link"
    
    @property
    def messages(self):
        return NotImplemented
