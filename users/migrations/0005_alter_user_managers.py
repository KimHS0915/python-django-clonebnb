# Generated by Django 3.2.9 on 2022-02-08 04:09

import common.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220127_1724'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', common.managers.CustomUserManager()),
            ],
        ),
    ]