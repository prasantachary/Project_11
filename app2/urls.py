from app2.views import *
from django.urls import path
app_name='specific'

urlpatterns=[
    path('mylife/',mylife,name='mylife'),
    path('kanha/',kanha,name='kanha'),
]