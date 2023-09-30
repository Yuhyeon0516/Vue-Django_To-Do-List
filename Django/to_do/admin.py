from django.contrib import admin

from to_do.models import Todo


# Register your models here.
@admin.register(Todo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "todo")
