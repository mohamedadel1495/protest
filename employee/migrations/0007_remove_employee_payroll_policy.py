# Generated by Django 5.0.6 on 2024-06-13 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_remove_employee_brithday_remove_employee_created_on_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='payroll_policy',
        ),
    ]
