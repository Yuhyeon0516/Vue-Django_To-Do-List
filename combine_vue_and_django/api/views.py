from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from todo.models import Todo


# Create your views here.
class ApiTodoLV(ListView):
    model = Todo

    def get(self, request, *args, **kwargs):
        tmpList = [
            {"id": 1, "name": "d김유현", "todo": "Django 와 Vue.js 연동 프로그램을 만들고 있습니다."},
            {"id": 2, "name": "d홍길동", "todo": "이름을 안쓰면 홍길동으로 나와요..."},
            {"id": 3, "name": "d이순신", "todo": "신에게는 아직 열두 척의 배가 있사옵니다."},
            {"id": 4, "name": "d성춘향", "todo": "그네 타기"},
        ]

        return JsonResponse(data=tmpList, safe=False)
