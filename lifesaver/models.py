from django.db import models

# Create your models here.

#Work Related aka Department and Work Shift

class Department(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class WorkShift(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name 

#Personel Related aka Employees and Patients

class Doctor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    work_shift = models.OneToOneField(WorkShift, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    sector = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    reports_to = models.ForeignKey(Doctor, blank=True, null=True, on_delete=models.CASCADE)
    work_shift = models.OneToOneField(WorkShift, default="", blank=True, null=True, on_delete=models.CASCADE)
    
    # in Nurse model
    def department_name(self):
        if self.sector_id:
            return self.sector.name
        else:
            return '' # or some other default

    def __str__(self):
         return self.name

class Patient(models.Model):
    STATUS = (
        ('Sick', 'Sick'),
        ('Healing', 'Healing'),
        ('Cured', 'Cured'),
        ('Deceased', 'Deceased'),
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
    department = models.ForeignKey(Department, default="", null=True, blank=True, on_delete=models.CASCADE)
    care = models.ForeignKey(Nurse, default="", blank=True, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
