from . import views
from django.urls import path

app_name = "todo"

urlpatterns = [
    path("vonly/", views.ToDoVueOnlyTV.as_view(), name="vonly"),
]
