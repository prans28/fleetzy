from django.urls import path
from . import views
urlpatterns=[path("",views.home,name="home"),path("request-demo/",views.request_demo,name="request-demo"),path("request-demo/success/",views.demo_success,name="demo-success")]
