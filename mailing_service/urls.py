from django.urls import path

from .views import (MailingCreateView, MailingDeleteView, MailingDetailView,
                    MailingUpdateView, MailingView, MessageCreateView,
                    MessageDeleteView, MessageDetailView, MessageUpdateView,
                    UserMailCreateView, UserMailDeleteView, UserMailDetailView,
                    UserMailUpdateView)

app_name = "mailing_service"


urlpatterns = [
    path("", MailingView.as_view(), name="home"),

    path("mailing_add/", MailingCreateView.as_view(), name="mailing_add"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("<int:pk>/update_mailing/", MailingUpdateView.as_view(), name="mailing_update"),
    path("<int:pk>/delete_mailing/", MailingDeleteView.as_view(), name="mailing_delete"),

    path("user_mail_create/", UserMailCreateView.as_view(), name="user_mail_create"),
    path("user_mail/<int:pk>/", UserMailDetailView.as_view(), name="user_mail_detail"),
    path("<int:pk>/update_user/", UserMailUpdateView.as_view(), name="user_mail_update"),
    path("<int:pk>/delete_user/", UserMailDeleteView.as_view(), name="user_mail_delete"),

    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("<int:pk>/update_message/", MessageUpdateView.as_view(), name="message_update"),
    path("<int:pk>/delete_message/", MessageDeleteView.as_view(), name="message_delete"),
]
