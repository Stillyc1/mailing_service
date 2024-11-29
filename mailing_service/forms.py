from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Mailing, UserMail, Message


class MailingForm(ModelForm):
    """Класс создания формы добавления рассылки"""
    class Meta:
        model = Mailing
        fields = "__all__"


class UserMailForm(ModelForm):
    """Класс создания формы добавления получателя рассылки"""
    class Meta:
        model = UserMail
        fields = "__all__"


class MessageForm(ModelForm):
    """Класс создания формы добавления письма"""
    class Meta:
        model = Message
        fields = "__all__"
