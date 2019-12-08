from django.shortcuts import render
from django.http import HttpResponse
from .models import Person,Pc_assets

# Create your views here.

def index(request):
    return HttpResponse("Hello, You're at the assets index.")

def persons(request,person_name):
    person = Person.objects.get(name=person_name)
    output = f'姓名{person_name},部门{person.department},职位{person.job_position}'
    return HttpResponse(output)
