from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Grades, Students
# 注册
admin.site.register(Grades)
admin.site.register(Students)
