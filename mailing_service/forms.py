from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Mailing


class MailingForm(ModelForm):
    """Класс создания формы добавления рассылки"""
    class Meta:
        model = Mailing
        fields = "__all__"
