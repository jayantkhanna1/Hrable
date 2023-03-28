from django.contrib import admin
from .models import HR, Employee, Admin, Jobs, Job_Application, Refferal, Quote, Query
# Register your models here.

admin.site.register(HR)
admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(Jobs)
admin.site.register(Job_Application)
admin.site.register(Refferal)
admin.site.register(Quote)
admin.site.register(Query)