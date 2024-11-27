# from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from mailing_service.models import UserMail, Mailing, Message, MailingAttempt


# Create your views here.
class MailingView(ListView):
    """Класс представления Всех рассылок на главной странице"""
    model = Mailing
    template_name = "mailing_service/home.html"
    context_object_name = "mailing"


class UserMailView(ListView):
    """Класс представления всех получателей рассылки"""
    model = UserMail
    template_name = "mailing_service/home.html"
    context_object_name = "user_mail"


class MessageView(ListView):
    """Класс представления Всех писем"""
    model = Message
    template_name = "mailing_service/home.html"
    context_object_name = "message"


class MailingAttemptView(ListView):
    """Класс представления Всех рассылок на главной странице"""
    model = MailingAttempt
    template_name = "mailing_service/home.html"
    context_object_name = "mailing_attempt"
