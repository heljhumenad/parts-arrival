from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy


from parts.core.mixins import MessageMixin

class UserCreateViewMixins(MessageMixin, generic.CreateView):
    messages = 'added'


class UserUpdateViewMixins(MessageMixin, generic.UpdateView):
    messages = 'updated'
