# Generated by Django 4.1.7 on 2023-09-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
