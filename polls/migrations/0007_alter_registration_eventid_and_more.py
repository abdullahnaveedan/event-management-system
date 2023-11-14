# Generated by Django 4.0.4 on 2023-11-13 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='eventid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.registeredevents'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
