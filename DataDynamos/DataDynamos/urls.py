
from django.contrib import admin
from django.urls import path
from EnvC.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('home/', home, name="home"),
    path('AQI/', AQI, name="    "),
    path('WQI/', WQI, name="WQI"),
    path('Environment/', Environment, name="Environment"),
    path('feedback/', feedback, name="feedback"),
    path('industry/', industry, name="industry"),
    path('About/', About, name="About"),
    path('nav/', nav, name="nav"),
    path('industry/success/', success, name="success"),
   

   
   


]
