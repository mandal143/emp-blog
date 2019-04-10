from django.conf.urls import include,url
from . import views
from rest_framework import routers, viewsets
from polls.views import *


router = routers.DefaultRouter()
router.register('', views.EmployeeViewSet)


urlpatterns = [
    
    
    url(r'^employee/', include(router.urls)),
    url(r'^login/$', views.login_api, name='login_api'),
    url(r'^sampleapi/$', views.sample_api, name='sample_api'),
        
]
    