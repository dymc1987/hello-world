from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Person,Pc_assets

# Create your views here.

def index(request):
    # return HttpResponse("Hello, You're at the assets index.")
    person = Person.objects.all()
    context = {'name':person}
    return render(request,'assets/index.html',context)

def assets(request,person_name):
    person = Person.objects.get(name=person_name)
    asset = get_object_or_404(Pc_assets,person_id=person_name)
    # context = {'asset':person.pc_assets_set.get(person_id=person_name)}
    # # 这里注意person.pc_assets_set的使用方法
    context = {'asset':asset}
    return render(request,'assets/assets.html',context)
