from django.urls import path
from . import views as t
from accounts import views as a
from home import views as h
urlpatterns = [
    path('',t.traveldesk_home,name='traveldesk_home'),
    path('car',t.car,name='car'),
    path('rent',t.rent,name='rent'),
    path('driver',t.driver,name='driver'),
    path('pick',t.pick,name='pick'),
    path('logout/',a.logout,name="logout"),
    path('login/',a.login,name="login"), 
 ]