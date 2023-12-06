from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def set(request):
    username = request.GET.get('username', 'Undefined')
    response = HttpResponse(f'Hello {username}!')
    response.set_cookie('username', username)
    return response

def get(request):
    username = request.COOKIES['username']
    return HttpResponse(f'Hello {username}!')

def index(request):
    nik = Person('Nik', 35)
    return JsonResponse(nik, safe=False, encoder=PersonEncoder)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest('Введены некорректные данные')
    if age > 17:
        return HttpResponse('Доступ разрешён')
    else:
        return HttpResponseForbidden('Доступ заблокирован: недостаточно лет')
