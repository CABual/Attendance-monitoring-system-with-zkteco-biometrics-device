# Generated by Django 5.0.4 on 2024-04-28 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biometrics', '0006_employee_birthplace_employee_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='data_hired',
            new_name='date_hired',
        ),
    ]