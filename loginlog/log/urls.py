from django.urls import path
from . import views
urlpatterns=[
    path("hello",views.qwe,name="name"),
    path('login',views.login,name='login')
]