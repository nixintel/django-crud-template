# Generated by Django 4.1.3 on 2022-12-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_vendor_emailformat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='emailformat',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
