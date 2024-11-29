from django.urls import path

from .views import MailingView, MailingDetailView, MailingUpdateView, MailingDeleteView, MailingCreateView

app_name = 'mailing_service'


urlpatterns = [
    path('', MailingView.as_view(), name='home'),

    path('mailing_add/', MailingCreateView.as_view(), name='mailing_add'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]
