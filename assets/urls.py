from django.urls import path

from . import views

app_name = 'assets'
urlpatterns = [
    path('', views.index, name='index'),
    path('<person_name>/', views.assets, name='assets'),
    path('add',views.add,name='add'),
    path('delete',views.delete,name='delete'),
    path('modify',views.modify,name='modify'),
    path('query',views.query,name='query'),
    path('additem', views.additem, name='additem'),
    # 这个path因为不需要真正被访问，只是作为form表单提交的对象，所以前面
    # 加一个名称与其他path区别开即可。
    path('deleteitem', views.deleteitem, name='deleteitem'),
    # 这个url跟上面的url同理。
    path('modifyitem', views.modifyitem, name='modifyitem'),
    # 这个url跟上面的url同理。
    path('queryitem', views.queryitem, name='queryitem'),
    # 这个url跟上面的url同理。
]
