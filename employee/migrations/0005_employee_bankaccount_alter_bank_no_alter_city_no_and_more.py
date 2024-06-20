# Generated by Django 5.0.6 on 2024-06-10 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_bank_college_costcenter_education_gender_gov_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bankaccount',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='city',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='college',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='costcenter',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='education',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='gender',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='gov',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='maritalstatus',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='militarystatus',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='region',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='team',
            name='no',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]