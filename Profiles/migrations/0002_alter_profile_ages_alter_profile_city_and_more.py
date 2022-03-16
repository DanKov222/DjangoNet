# Generated by Django 4.0.2 on 2022-03-01 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ages',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
