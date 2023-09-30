from django.views.generic import TemplateView

# Create your views here.


class ToDoVueOnlyTV(TemplateView):
    template_name = "todo/todo_vue_only.html"
