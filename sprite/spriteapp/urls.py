from . import views
from django.urls import path



urlpatterns = [

    path('',views.demo,name='demo'),
    path('demo1/',views.demo1,name='demo1'),
    # path('add/',views.demo1,name='demo1'),
    #path('add/',views.addition,name='addition')
]
