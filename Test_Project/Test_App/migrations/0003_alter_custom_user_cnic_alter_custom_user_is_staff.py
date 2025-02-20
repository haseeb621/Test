# Generated by Django 5.1 on 2025-02-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_App', '0002_rename_cinc_custom_user_cnic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='cnic',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
