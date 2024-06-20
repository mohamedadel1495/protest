from django.db import models
import datetime
from django.shortcuts import render
import _uuid
from users.models import User
from payroll.models import *
from django.core.validators import MaxValueValidator

class Department(models.Model):
    no = models.IntegerField(validators=[MaxValueValidator(99)],default=0)
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Section(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    department = models.ForeignKey(Department,related_name='section_department',on_delete=models.PROTECT)
    created_on = models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Education(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class College(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    education = models.ForeignKey(Education,related_name='college_education',on_delete=models.PROTECT)
    created_on = models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Specialty(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    college = models.ForeignKey(College,related_name='specialty_specialty',on_delete=models.PROTECT)
    created_on = models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Bank(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on = models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class CostCenter(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on = models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Team(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on = models.DateField(auto_now_add=True)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class JobTitle(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Region(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Gender(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class MaritalStatus(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class MilitaryStatus(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Gov(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    stat=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class City(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50)
    created_on=models.DateField(auto_now_add=True)
    stat=models.BooleanField(default=True)
    gov = models.ForeignKey(Gov, related_name='City_Gov',on_delete=models.PROTECT)
    def __str__(self):
        return self.name
class Employee(models.Model):
    name = models.CharField(max_length=120)
    code = models.IntegerField(unique=True)
    phone = models.CharField(max_length=12)
    national_id = models.IntegerField(validators=[MaxValueValidator(99999999999999)], default=0)
    email = models.EmailField(max_length=50, null=True)
    brithday = models.DateField(default=datetime.datetime.now)
    hiredate = models.DateField(default=datetime.datetime.now)
    hint = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=120, null=True,blank=True)
    gov = models.ForeignKey(Gov,related_name='employee_gov', null=True,on_delete=models.PROTECT)
    city = models.ForeignKey(City,related_name='employee_city', null=True,on_delete=models.PROTECT)
    education = models.ForeignKey(Education,related_name='employee_education', null=True,on_delete=models.PROTECT)
    college = models.ForeignKey(College,related_name='employee_college', null=True,on_delete=models.PROTECT)
    specialty = models.ForeignKey(Specialty,related_name='employee_specialty', null=True,on_delete=models.PROTECT)
    gender = models.ForeignKey(Gender,related_name='employee_gender',on_delete=models.PROTECT, null=True)
    maritalstatus = models.ForeignKey(MaritalStatus,related_name='employee_marital',on_delete=models.PROTECT, null=True)
    militarystatus = models.ForeignKey(MilitaryStatus,related_name='employee_military',on_delete=models.PROTECT, null=True)
    region = models.ForeignKey(Region,related_name='employee_region',on_delete=models.PROTECT, null=True)
    jobtitle = models.ForeignKey(JobTitle,related_name='employee_jobtitle', null=True,on_delete=models.PROTECT)
    team = models.ForeignKey(Team,related_name='employee_team', null=True,on_delete=models.PROTECT)
    costcenter = models.ForeignKey(CostCenter,related_name='employee_cost',on_delete=models.PROTECT, null=True)
    payrollpolicy = models.ForeignKey(PayrollPolicy,related_name='employee_cost',on_delete=models.PROTECT, null=True)
    bank = models.ForeignKey(Bank, related_name='employee_bank',null=True,on_delete=models.PROTECT)
    bankaccount = models.IntegerField(unique=True, null=True)
    department = models.ForeignKey(Department, related_name='employee_department',on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, related_name='employee_section', on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE, null=True)
    # created_on = models.DateField(default=datetime.datetime.now)
    stat = models.BooleanField(default=True)

    def __str__(self):
        return self.name