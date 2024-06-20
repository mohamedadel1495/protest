from django.db import models
import datetime
from django.shortcuts import render
import _uuid
from users.models import User
from django.core.validators import MaxValueValidator

class Payroll(models.Model):
    no = models.IntegerField(validators=[MaxValueValidator(99)])
    basic = models.DecimalField(max_digits=10, decimal_places=2)
    additinal = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    incentives = models.DecimalField(max_digits=10, decimal_places=2)
    expensive = models.DecimalField(max_digits=10, decimal_places=2)
    changes = models.DecimalField(max_digits=10, decimal_places=2)
    home = models.DecimalField(max_digits=10, decimal_places=2)
    trans = models.DecimalField(max_digits=10, decimal_places=2)
    nature = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name

class PayrollPolicy(models.Model):
    no = models.IntegerField(validators=[MaxValueValidator(99)])
    name = models.CharField(unique=True, max_length=45)
    overtime = models.FloatField(max_length=4, default=1.7)
    overdays = models.FloatField(max_length=4, default=2)
    monthdays = models.FloatField(max_length=2, default=30)
    dailyhours = models.FloatField(max_length=2, default=8)
    late = models.BooleanField(default=False)
    early = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class PayrollTemplates(models.Model):
    no = models.IntegerField(validators=[MaxValueValidator(99)])
    name = models.CharField(unique=True, max_length=45)
    basic = models.DecimalField(max_digits=10, decimal_places=2)
    additinal = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    incentives = models.DecimalField(max_digits=10, decimal_places=2)
    expensive = models.DecimalField(max_digits=10, decimal_places=2)
    changes = models.DecimalField(max_digits=10, decimal_places=2)
    home = models.DecimalField(max_digits=10, decimal_places=2)
    trans = models.DecimalField(max_digits=10, decimal_places=2)
    nature = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Payrolli(models.Model):
    no = models.IntegerField(validators=[MaxValueValidator(99)])
    name = models.CharField(unique=True, max_length=45)
    dbname = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Payrollmonth(models.Model):
    date = models.DateField()
    abasic = models.DecimalField(max_digits=10, decimal_places=2)
    aadditinal = models.DecimalField(max_digits=10, decimal_places=2)
    abonus = models.DecimalField(max_digits=10, decimal_places=2)
    aincentives = models.DecimalField(max_digits=10, decimal_places=2)
    aexpensive = models.DecimalField(max_digits=10, decimal_places=2)
    achanges = models.DecimalField(max_digits=10, decimal_places=2)
    ahome = models.DecimalField(max_digits=10, decimal_places=2)
    atrans = models.DecimalField(max_digits=10, decimal_places=2)
    anature = models.DecimalField(max_digits=10, decimal_places=2)
    afood = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Payrollt(models.Model):
    name = models.CharField(unique=True, max_length=45)
    basic = models.FloatField(default=0)
    vbasic = models.FloatField(default=0)
    nbasic = models.FloatField(default=0)
    additinal = models.FloatField(default=0)
    vadditinal = models.FloatField(default=0)
    nadditinal = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    vbonus = models.FloatField(default=0)
    nbonus = models.FloatField(default=0)
    incentives = models.FloatField(default=0)
    vincentives = models.FloatField(default=0)
    nincentives = models.FloatField(default=0)
    expensive = models.FloatField(default=0)
    vexpensive = models.FloatField(default=0)
    nexpensive = models.FloatField(default=0)
    changes = models.FloatField(default=0)
    vchanges = models.FloatField(default=0)
    nchanges = models.FloatField(default=0)
    home = models.FloatField(default=0)
    vhome = models.FloatField(default=0)
    nhome = models.FloatField(default=0)
    trans = models.FloatField(default=0)
    vtrans = models.FloatField(default=0)
    ntrans = models.FloatField(default=0)
    nature = models.FloatField(default=0)
    vnature = models.FloatField(default=0)
    nnature = models.FloatField(default=0)
    food = models.FloatField(default=0)
    vfood = models.FloatField(default=0)
    nfood = models.FloatField(default=0)
    datef = models.DateField(default=0)
    datet = models.DateField(default=0)

    def __str__(self):
        return self.name
