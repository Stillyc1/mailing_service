from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailing_service.forms import MailingForm, UserMailForm, MessageForm
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
    context_object_name = "mailing_update"

    fields = "__all__"

    def get_success_url(self):
        return reverse('mailing_service:mailing_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    """Класс представления удаления рассылки"""
    model = Mailing
    template_name = "mailing_service/mailing_delete.html"
    context_object_name = "mailing_delete"

    success_url = reverse_lazy('mailing_service:home')


class UserMailDetailView(DetailView):
    """Класс представления детально получателя рассылки"""
    model = UserMail
    template_name = "mailing_service/user_mail_detail.html"
    context_object_name = "user_mail_detail"


class UserMailCreateView(CreateView):
    """Класс представления создания получателей рассылки"""
    model = UserMail
    template_name = "mailing_service/user_mail_create.html"
    context_object_name = "user_mail_create"

    form_class = UserMailForm
    success_url = reverse_lazy('mailing_service:home')


class UserMailUpdateView(UpdateView):
    """Класс представления обновления получателей рассылки"""
    model = UserMail
    template_name = "mailing_service/user_mail_create.html"
    context_object_name = "user_mail_update"

    fields = "__all__"

    def get_success_url(self):
        return reverse('mailing_service:user_mail_detail', args=[self.kwargs.get('pk')])


class UserMailDeleteView(DeleteView):
    """Класс представления удаления получателей рассылки"""
    model = UserMail
    template_name = "mailing_service/user_mail_confirm_delete.html"
    context_object_name = "user_mail_delete"

    success_url = reverse_lazy('mailing_service:home')


class MessageDetailView(DetailView):
    """Класс представления писем"""
    model = Message
    template_name = "mailing_service/message_detail.html"
    context_object_name = "message_detail"


class MessageCreateView(CreateView):
    """Класс представления создания писем"""
    model = Message
    template_name = "mailing_service/message_create.html"
    context_object_name = "message_create"

    form_class = MessageForm
    success_url = reverse_lazy('mailing_service:home')


class MessageUpdateView(UpdateView):
    """Класс представления обновления писем"""
    model = Message
    template_name = "mailing_service/message_create.html"
    context_object_name = "message_update"

    fields = "__all__"

    def get_success_url(self):
        return reverse('mailing_service:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    """Класс представления удаления писем"""
    model = Message
    # template_name = "mailing_service/message_confirm_delete.html"
    context_object_name = "message_delete"

    success_url = reverse_lazy('mailing_service:home')


class MailingAttemptView(ListView):
    """Класс представления Всех рассылок на главной странице"""
    model = MailingAttempt
    template_name = "mailing_service/home.html"
    context_object_name = "mailing_attempt"
