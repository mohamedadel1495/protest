from django.db import models
import datetime
from django.shortcuts import render
import _uuid
from users.models import User
from django.core.validators import MaxValueValidator

# Create your models here.


class Machines(models.Model):
    no = models.IntegerField(default=0,validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50,unique=True)
    ip = models.CharField(max_length=50,unique=True)
    port = models.IntegerField(default=4370)
    password = models.CharField(default=0)
    date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_on=models.DateField(auto_now_add=True,default=datetime.datetime.now())
    stat=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Tempattend(models.Model):
    code = models.CharField(max_length=45)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    present = models.CharField(max_length=45, blank=True, null=True)
    come_late = models.CharField(max_length=9, blank=True, null=True)
    going_early = models.CharField(max_length=9, blank=True, null=True)
    shiftname = models.CharField(max_length=45, blank=True, null=True)
    overday = models.IntegerField(blank=True, null=True)
    cancel = models.IntegerField(blank=True, null=True)
    unq = models.CharField(unique=True, max_length=45, blank=True, null=True)

class Attendance(models.Model):
    code = models.PositiveIntegerField(blank=True, null=True)
    check_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    machines = models.ForeignKey(Machines, related_name='attendance_machines', on_delete=models.CASCADE, null=True)
    isclac = models.IntegerField(blank=True, null=True)
    idmission = models.IntegerField()
    note = models.CharField(max_length=45, blank=True, null=True)