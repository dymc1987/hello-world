from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Person,Pc_assets

# Create your views here.

def index(request):
    # return HttpResponse("Hello, You're at the assets index.")
    li = []
    person = Person.objects.all()
    # 取出Person表中的所有对象
    for p in person:
        pc = p.pc_assets_set.all().values()
        # 针对Person表中的每一个对象，去Pc_assets表中查询关联内容，并生成列表
        for i in range(0,len(pc)):
        # 针对Pc_assets表中与Person表中对象相关联数据的条数(1对多关系)，
        # 对数据进行逐条组合，以便于使用
            dic = {
                'name':p.name, 
                'department':p.department,
                'job_position':p.job_position,
                'pc_type':pc[i]['pc_type'],
                # 取出列表中的字典，再根据字典的key，取出value
                'sn':pc[i]['sn']
            }
            li.append(dic)      
    i = 1
    for l in li:
        if i % 5 == 1:
            l['class'] = 'table-success'
        elif i % 5 == 2:
            l['class'] = 'table-danger'
        elif i % 5 == 3:
            l['class'] = 'table-warning'
        elif i % 5 == 4:
            l['class'] = 'table-info'
        elif i % 5 == 0:
            l['class'] = 'table-light'
        else:
            pass
        i += 1  
    # print(li) 
    context = {'li':li}
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

def additem(request):
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
        # 的数据不能为空，后者不允许为空，为空则会报错(也可以用try来规避这一问题)。
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
    





