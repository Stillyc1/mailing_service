# Generated by Django 5.1.3 on 2024-12-04 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_service", "0004_alter_mailingattempt_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "ordering": ["date_start", "date_end", "status", "message"],
                "permissions": [("can_view_mailing", "can view mailing")],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.AlterModelOptions(
            name="mailingattempt",
            options={
                "ordering": ["datetime_attempt", "status", "mail_response", "mailing"],
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылки",
            },
        ),
        migrations.AlterModelOptions(
            name="message",
            options={
                "ordering": ["head_letter", "body_letter"],
                "permissions": [("can_view_message", "can view message")],
                "verbose_name": "Письмо",
                "verbose_name_plural": "Письма",
            },
        ),
        migrations.AlterModelOptions(
            name="usermail",
            options={
                "ordering": ["email", "fullname"],
                "permissions": [("can_view_user_mail", "can view user_mail")],
                "verbose_name": "Получатель",
                "verbose_name_plural": "Получатели",
            },
        ),
    ]