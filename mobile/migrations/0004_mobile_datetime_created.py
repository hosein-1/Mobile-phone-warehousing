# Generated by Django 5.0.7 on 2024-08-03 16:05

import django.utils.timezone
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_alter_mobile_screen_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='datetime_created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
