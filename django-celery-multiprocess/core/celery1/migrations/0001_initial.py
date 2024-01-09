# Generated by Django 4.1.7 on 2023-09-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('body', models.TextField(default='')),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
