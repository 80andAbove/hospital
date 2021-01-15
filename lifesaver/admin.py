from django.contrib import admin
from .models import *

# Register your models here.

#Work Related
admin.site.register(Department)
admin.site.register(WorkShift)

#Personel Related
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)