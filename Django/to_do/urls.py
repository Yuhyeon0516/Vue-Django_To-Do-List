from . import views
from django.urls import path

app_name = "todo"

urlpatterns = [
    path("vonly/", views.ToDoVueOnlyTV.as_view(), name="vonly"),
    path("create/", views.ToDoCV.as_view(), name="create"),
    path("list/", views.ToDoLV.as_view(), name="list"),
    path("<int:pk>/delete/", views.ToDoDelV.as_view(), name="delete"),
    path("mixin/", views.ToDoMOMCV.as_view(), name="mixin"),
]
