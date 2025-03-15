
from django.contrib import admin # type: ignore
from. models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task', 'completed', 'update')
    
admin.site.register(Task, TaskAdmin)