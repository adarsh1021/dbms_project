from django.conf.urls import url,include
from django.contrib import admin
from tc_app import views 

urlpatterns = [
	url(r'^index/',views.index,name='index'),
	url(r'^get_element/',views.get_element,name='get_element'),

]