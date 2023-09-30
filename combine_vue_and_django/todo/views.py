from django.views.generic import TemplateView


# Create your views here.
class TodoTV(TemplateView):
    template_name = "todo/todo_index.html"
