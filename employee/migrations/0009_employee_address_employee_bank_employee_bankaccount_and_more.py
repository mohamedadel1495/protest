# Generated by Django 5.0.6 on 2024-06-13 20:43

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_remove_employee_address_remove_employee_bank_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_bank', to='employee.bank'),
        ),
        migrations.AddField(
            model_name='employee',
            name='bankaccount',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='brithday',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_city', to='employee.city'),
        ),
        migrations.AddField(
            model_name='employee',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_college', to='employee.college'),
        ),
        migrations.AddField(
            model_name='employee',
            name='costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_cost', to='employee.costcenter'),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_on',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_department', to='employee.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='education',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_education', to='employee.education'),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_gender', to='employee.gender'),
        ),
        migrations.AddField(
            model_name='employee',
            name='gov',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_gov', to='employee.gov'),
        ),
        migrations.AddField(
            model_name='employee',
            name='hint',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='hiredate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='jobtitle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_jobtitle', to='employee.jobtitle'),
        ),
        migrations.AddField(
            model_name='employee',
            name='maritalstatus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_marital', to='employee.maritalstatus'),
        ),
        migrations.AddField(
            model_name='employee',
            name='militarystatus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_military', to='employee.militarystatus'),
        ),
        migrations.AddField(
            model_name='employee',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_region', to='employee.region'),
        ),
        migrations.AddField(
            model_name='employee',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_section', to='employee.section'),
        ),
        migrations.AddField(
            model_name='employee',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_specialty', to='employee.specialty'),
        ),
        migrations.AddField(
            model_name='employee',
            name='stat',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_team', to='employee.team'),
        ),
    ]
