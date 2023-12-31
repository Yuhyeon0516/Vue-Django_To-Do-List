from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from to_do.models import Todo

# Create your views here.


class ToDoVueOnlyTV(TemplateView):
    template_name = "todo/todo_vue_only.html"


class ToDoCV(CreateView):
    model = Todo
    fields = "__all__"
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo:list")


class ToDoLV(ListView):
    model = Todo
    template_name = "todo/todo_list.html"


class ToDoDelV(DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy("todo:list")


class ToDoMOMCV(MultipleObjectMixin, CreateView):
    model = Todo
    fields = "__all__"
    template_name = "todo/todo_form_list.html"
    success_url = reverse_lazy("todo:mixin")

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)


class ToDoDelV2(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo:mixin")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
