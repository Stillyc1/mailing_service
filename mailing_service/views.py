from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailing_service.forms import MailingForm
from mailing_service.models import UserMail, Mailing, Message, MailingAttempt


class MailingView(ListView):
    """Класс представления Всех рассылок на главной странице"""
    model = Mailing
    template_name = "mailing_service/home.html"
    context_object_name = "mailing"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_mail'] = UserMail.objects.all()
        context['mailing_all_started'] = Mailing.objects.filter(status='started')

        return context


class MailingCreateView(CreateView):
    """Класс представления создания рассылки"""
    model = Mailing
    template_name = "mailing_service/mailing_add.html"
    context_object_name = "mailing_add"

    form_class = MailingForm
    success_url = reverse_lazy('mailing_service:home')


class MailingDetailView(DetailView):
    """Класс представления детальной рассылки"""
    model = Mailing
    template_name = "mailing_service/mailing_detail.html"
    context_object_name = "mailing_detail"


class MailingUpdateView(UpdateView):
    """Класс представления обновления рассылки"""
    model = Mailing
    template_name = "mailing_service/mailing_add.html"
    context_object_name = "mailing_add"

    fields = "__all__"

    def get_success_url(self):
        return reverse('mailing_service:mailing_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    """Класс представления удаления рассылки"""
    model = Mailing
    template_name = "mailing_service/mailing_delete.html"
    context_object_name = "mailing_delete"

    success_url = reverse_lazy('mailing_service:home')


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
