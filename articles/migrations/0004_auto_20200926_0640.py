# Generated by Django 3.1 on 2020-09-26 03:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_forensic_machine_security_tools'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Machine',
            new_name='Translate',
        ),
    ]
