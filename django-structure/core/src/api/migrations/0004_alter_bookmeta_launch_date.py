# Generated by Django 4.2.8 on 2024-01-08 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_bookmeta_book_alter_bookmeta_launch_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmeta',
            name='launch_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 15, 45, 35, 201405)),
        ),
    ]
