# Generated by Django 4.0.2 on 2022-02-24 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localpost',
            options={'ordering': ['-date']},
        ),
    ]