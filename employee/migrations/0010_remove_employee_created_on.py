# Generated by Django 5.0.6 on 2024-06-13 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_employee_address_employee_bank_employee_bankaccount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_on',
        ),
    ]
