from django.views import generic
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.contrib.auth import views 

from parts.app.forms import auth_forms
from parts.app.accounts.models import CustomUser


class AccountTemplateView(generic.TemplateView):
    template_name = "accounts/index.html"


class AccountLoginView(views.LoginView):
    template = "accounts/login.html"


# TODO
# Fix Logout that can use to redirect logout without authentication
class AccountLogoutView(views.LogoutView):
    template_name = "registration/logout.html"


class AccountEditView(generic.UpdateView):
    template_name = "accounts/update_user.html"
    success_url = reverse_lazy("accounts:edit_user")
    context_object_name = "user"
    form_class = auth_forms.CustomUserChangeForm

    def get_object(self, query_pk_and_slug=None):
        user = CustomUser.objects.filter(id=self.kwargs["pk"]).first()
        return user


# TODO fix bug updating password from other account
class AccountChangePasswordView(views.PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:edit_user")
    form_class = auth_forms.AccountPasswordChangeForm
