from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import BaseDeleteView
from django.views.generic.list import BaseListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo


# Create your views here.
class ApiTodoLV(BaseListView):
    model = Todo

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context["object_list"].values())

        return JsonResponse(data=todoList, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class ApiTodoDelV(BaseDeleteView):
    model = Todo

    def delete(self, request, *args, **kwarg):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)
