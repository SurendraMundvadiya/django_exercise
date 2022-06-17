# Generated by Django 4.0.4 on 2022-06-17 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
