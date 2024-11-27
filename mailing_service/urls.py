from django.urls import path

from .views import MailingView

app_name = 'mailing_service'


urlpatterns = [
    path('', MailingView.as_view(), name='show_home'),
]
