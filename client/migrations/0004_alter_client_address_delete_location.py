# Generated by Django 4.1.4 on 2022-12-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_location_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]