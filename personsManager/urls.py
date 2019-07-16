from django.contrib import admin  
from personsManager import views  
from django.conf.urls import url

urlpatterns = [   
     url(r'emp',views.emp),
     url(r'show',views.show),  
     url(r'^edit/(?P<id>\d+)/$',views.edit),  
     url(r'^update/(?P<id>\d+)$',views.update),  
     url(r'^delete/(?P<id>\d+)/$',views.destroy),  
]  