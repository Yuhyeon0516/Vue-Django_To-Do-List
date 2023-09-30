import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic.edit import BaseDeleteView, BaseCreateView
from django.views.generic.list import BaseListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from todo.models import Todo


# Create your views here.
@method_decorator(ensure_csrf_cookie, name="dispatch")
class ApiTodoLV(BaseListView):
    model = Todo

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context["object_list"].values())

        return JsonResponse(data=todoList, safe=False)


class ApiTodoDelV(BaseDeleteView):
    model = Todo

    def delete(self, request, *args, **kwarg):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)


class ApiTodoCV(BaseCreateView):
    model = Todo
    fields = "__all__"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["data"] = json.loads(self.request.body)

        return kwargs

    def form_valid(self, form):
        self.object = form.save()

        newTodo = model_to_dict(self.object)

        return JsonResponse(data=newTodo, status=201)

    def form_invalid(self, form):
        return JsonResponse(data=form.errors, status=400)
