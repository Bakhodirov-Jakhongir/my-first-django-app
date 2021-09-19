from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('some/api/', views.index, name='index'),
    path('hello/' , views.sayHello , name='sayHello')
]