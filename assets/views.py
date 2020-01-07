from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Person,Pc_assets
from .format import format,pc_format

# Create your views here.

person = Person.objects.all()
# 取出Person表中的所有对象

def index(request):
    context = format(person)
    # 调用format函数，将人员信息格式化为想要的数据格式
    return render(request,'assets/index.html',context)

def assets(request,person_name):
    person = Person.objects.get(name=person_name)
    asset = get_object_or_404(Pc_assets,person_id=person_name)
    # context = {'asset':person.pc_assets_set.get(person_id=person_name)}
    # # 这里注意person.pc_assets_set的使用方法
    context = {'asset':asset}
    return render(request,'assets/assets.html',context)

def add(request):
    return render(request,'assets/add.html')

def delete(request):
    return render(request,'assets/delete.html')

def modify(request):
    return render(request,'assets/modify.html')

def query(request):
    return render(request,'assets/query.html')

def additem(request):
    if Person.objects.get(name=request.POST['name']):
        person = Person.objects.get(name=request.POST['name'])
        person.pc_assets_set.create(pc_type=request.POST['pc_type'],sn=request.POST['sn'])
    else:
        person = Person.objects.create(name=request.POST['name'])
        person.department = request.POST['department']
        person.job_position = request.POST['job_position']
        person.save()
        person.pc_assets_set.create(pc_type=request.POST['pc_type'],sn=request.POST['sn'])
    return HttpResponseRedirect(reverse('assets:index'))

def deleteitem(request):
    if request.POST.get('name'):
        # 如果前端提交过来的是name信息
        # request.POST.get('name')与request.POST['name']作用相同，区别是前者允许前端提交过来
        # 的数据为空，后者不允许为空，为空则会报错(也可以用try来规避这一问题)。
        person = Person.objects.get(name=request.POST['name'])
        person.delete()
    elif request.POST.get('sn'):
        # 如果前端提交过来的是sn信息
        pc = Pc_assets.objects.get(sn=request.POST['sn'])
        pc.delete()
    return HttpResponseRedirect(reverse('assets:index'))

def modifyitem(request):
    person = Person.objects.all()
    li = [p.name for p in person]
    if request.POST.get('name') not in li:
        context = {
            'warning':'糟糕！',
            'notification':'找不到这个用户',
        }
        return render(request,'assets/notice.html',context)

def queryitem(request):
    if request.POST.get('name'):
        person = Person.objects.filter(name=request.POST['name'])
        # 根据前端提交的name，来查询人员信息，这里一定要用filter
        context = format(person)
        # 调用format函数，将人员信息格式化为想要的数据格式
        return render(request,'assets/index.html',context)
    elif request.POST.get('department'):
        person = Person.objects.filter(department=request.POST['department'])
        context = format(person)
        return render(request,'assets/index.html',context)
    elif request.POST.get('sn'):
        pc = Pc_assets.objects.filter(sn=request.POST['sn'])
        # 用filter，即便只有一个数据，也会是iterator，可直接用于for循环
        # li = []
        # li.append(pc)
        context = pc_format(pc)
        return render(request,'assets/index.html',context)
    elif request.POST.get('pc_type'):
        pc = Pc_assets.objects.filter(pc_type=request.POST['pc_type'])
        context = pc_format(pc)
        return render(request,'assets/index.html',context)

