from .models import Person,Pc_assets

def format(data):
    li = []
    num = 1
    for p in data:
        pc = p.pc_assets_set.all().values()
        # 针对Person表中的每一个对象，去Pc_assets表中查询关联内容，并生成列表
        for i in range(0,len(pc)):
        # 针对Pc_assets表中与Person表中对象相关联数据的条数(1对多关系)，
        # 对数据进行逐条组合，以便于使用
            dic = {
                'num':num,
                'name':p.name, 
                'department':p.department,
                'job_position':p.job_position,
                'pc_type':pc[i]['pc_type'],
                # 取出列表中的字典，再根据字典的key，取出value
                'sn':pc[i]['sn']
            }
            li.append(dic)
            num += 1      
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
    return {'li':li}

def pc_format(data):
    li = []
    num = 1
    for p in data:
        name = p.person_id
        person = Person.objects.get(name=name)
        dic = {
            'num':num,
            'name':name, 
            'department':person.department,
            'job_position':person.job_position,
            'pc_type':p.pc_type,
            'sn':p.sn
        }
        li.append(dic)
        num += 1      
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
    return {'li':li}