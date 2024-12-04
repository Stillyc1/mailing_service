from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from mailing_service.forms import MailingForm, MessageForm, UserMailForm
from mailing_service.models import Mailing, MailingAttempt, Message, UserMail
from users.models import CustomUser


class MailingView(ListView):
    """Класс представления Всех рассылок на главной странице"""

    model = Mailing
    template_name = "mailing_service/home.html"
    context_object_name = "mailing"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["user_mail"] = UserMail.objects.all()
        context["mailing_all_started"] = Mailing.objects.filter(status="Запущена")

        if self.request.user.is_authenticated:
            context['user_usermail'] = UserMail.objects.filter(owner=self.request.user)
            context['user_message'] = Message.objects.filter(owner=self.request.user)
            context['user_mailing_started'] = Mailing.objects.filter(owner=self.request.user, status='Запущена')
            context['user_mailing'] = Mailing.objects.filter(owner=self.request.user)
            context['user_mailingattempt'] = MailingAttempt.objects.filter(owner=self.request.user)

        return context


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Класс представления создания рассылки"""

    model = Mailing
    template_name = "mailing_service/mailing_add.html"
    context_object_name = "mailing_add"

    form_class = MailingForm
    success_url = reverse_lazy("mailing_service:mailing_detail")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user

        mailing.save()
        return super().form_valid(form)


class MailingDetailView(LoginRequiredMixin, ListView):
    """Класс представления детальной рассылки"""

    model = Mailing
    template_name = "mailing_service/mailing_detail.html"
    context_object_name = "mailing_detail"

    def get_queryset(self):
        user = self.request.user

        if user.has_perm('mailing_service.can_view_mailing'):
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=user)

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.owner or user.has_perm('catalog.delete_product'):
    #         return super().get_form_class()
    #     raise PermissionDenied

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner == self.request.user:
    #         return self.object
    #     raise PermissionDenied


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представления обновления рассылки"""

    model = Mailing
    template_name = "mailing_service/mailing_add.html"
    context_object_name = "mailing_update"

    form_class = MailingForm

    def get_success_url(self):
        return reverse("mailing_service:mailing_detail")

    def get_form_class(self):
        """
        Проверка чтобы пользователь был владельцем продукта и тогда может его изменять
        и если у пользовтаеля есть право can_unpublish_product
        """
        user = self.request.user
        if user == self.object.owner:
            return MailingForm
        raise PermissionDenied


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представления удаления рассылки"""

    model = Mailing
    template_name = "mailing_service/mailing_delete.html"
    context_object_name = "mailing_delete"

    success_url = reverse_lazy("mailing_service:mailing_detail")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return super().get_form_class()
        raise PermissionDenied


class UserMailDetailView(LoginRequiredMixin, ListView):
    """Класс представления детально получателя рассылки"""

    model = UserMail
    template_name = "mailing_service/user_mail_detail.html"
    context_object_name = "user_mail_detail"

    def get_queryset(self):
        user = self.request.user

        if user.has_perm('mailing_service.can_view_user_mail'):
            return UserMail.objects.all()
        return UserMail.objects.filter(owner=user)

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner == self.request.user:
    #         return self.object
    #     raise PermissionDenied


class UserMailCreateView(LoginRequiredMixin, CreateView):
    """Класс представления создания получателей рассылки"""

    model = UserMail
    template_name = "mailing_service/user_mail_create.html"
    context_object_name = "user_mail_create"

    form_class = UserMailForm
    success_url = reverse_lazy("mailing_service:user_mail_detail")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()

        return super().form_valid(form)


class UserMailUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представления обновления получателей рассылки"""

    model = UserMail
    template_name = "mailing_service/user_mail_create.html"
    context_object_name = "user_mail_update"

    form_class = UserMailForm

    def get_success_url(self):
        return reverse("mailing_service:user_mail_detail")

    def get_form_class(self):
        """
        Проверка чтобы пользователь был владельцем продукта и тогда может его изменять
        и если у пользовтаеля есть право can_unpublish_product
        """
        user = self.request.user
        if user == self.object.owner:
            return UserMailForm
        raise PermissionDenied


class UserMailDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представления удаления получателей рассылки"""

    model = UserMail
    template_name = "mailing_service/user_mail_confirm_delete.html"
    context_object_name = "user_mail_delete"

    success_url = reverse_lazy("mailing_service:user_mail_detail")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return super().get_form_class()
        raise PermissionDenied


class MessageDetailView(LoginRequiredMixin, ListView):
    """Класс представления писем"""

    model = Message
    template_name = "mailing_service/message_detail.html"
    context_object_name = "message_detail"

    def get_queryset(self):
        user = self.request.user

        if user.has_perm('mailing_service.can_view_message'):
            return Message.objects.all()
        return Message.objects.filter(owner=user)

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner == self.request.user:
    #         return self.object
    #     raise PermissionDenied


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Класс представления создания писем"""

    model = Message
    template_name = "mailing_service/message_create.html"
    context_object_name = "message_create"

    form_class = MessageForm
    success_url = reverse_lazy("mailing_service:message_detail")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представления обновления писем"""

    model = Message
    template_name = "mailing_service/message_create.html"
    context_object_name = "message_update"

    form_class = MessageForm

    def get_success_url(self):
        return reverse("mailing_service:message_detail")

    def get_form_class(self):
        """
        Проверка чтобы пользователь был владельцем продукта и тогда может его изменять
        и если у пользовтаеля есть право can_unpublish_product
        """
        user = self.request.user
        if user == self.object.owner:
            return MessageForm
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представления удаления писем"""

    model = Message
    context_object_name = "message_delete"

    success_url = reverse_lazy("mailing_service:message_detail")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return super().get_form_class()
        raise PermissionDenied


class MailingAttemptView(LoginRequiredMixin, ListView):
    """Класс представления Всех рассылок на главной странице"""

    model = MailingAttempt
    template_name = "mailing_service/mailing_attempt_detail.html"
    context_object_name = "mailing_attempt"

    def get_queryset(self):
        return MailingAttempt.objects.filter(owner=self.request.user)

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner == self.request.user:
    #         return self.object
    #     raise PermissionDenied


class UserRegisterView(LoginRequiredMixin, ListView):
    """Класс представления Всех рассылок на главной странице"""

    model = CustomUser
    template_name = "mailing_service/user_register_view.html"
    context_object_name = "users"

    def get_queryset(self):
        user = self.request.user

        if user.has_perm('users.can_ban_user'):
            return CustomUser.objects.all()
        return PermissionDenied


class UserBanView(LoginRequiredMixin, DeleteView):
    """Класс представления Всех рассылок на главной странице"""

    model = CustomUser
    template_name = "mailing_service/user_register_ban.html"
    context_object_name = "user_ban"
    success_url = reverse_lazy("mailing_service:users_register")

    def get_queryset(self):
        user = self.request.user

        if user.has_perm('users.can_ban_user'):
            return CustomUser.objects.all()
        return PermissionDenied

    def form_valid(self, form):
        success_url = self.get_success_url()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(success_url)
