# Generated by Django 5.1.3 on 2024-12-04 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_customuser_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={
                "permissions": [
                    ("can_ban_user", "can ban user"),
                    ("can_stop_mailing", "can stop mailing"),
                ],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]