# Generated by Django 4.1.3 on 2022-12-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='emailformat',
            field=models.EmailField(default=True, max_length=100),
        ),
    ]
