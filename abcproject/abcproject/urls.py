"""abcproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls import patterns


  
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.index, name='index'),
  url(r'^/save_prospect_info$', views.index, name='index'),
]
  # url(r'^$', views.index, name='index'),
  # # url(r'^$', views.home, name='home'),
  # url(r'^login$', views.login_user, name='login_user'),
  # url(r'^register$', views.register, name='register'),
  # url(r'^logout$', views.logout_user, name='logout_user'),
  # url(r'^employees/', include('employees.urls', namespace = 'employees')),
  # url(r'^upload', views.handle_uploaded_file, name='handle_uploaded_file'), 
#   url(r'^upload_file', 'employees.views.upload_file', name='upload_file'),
#   url(r'^(?P<id>[0-9]+)/', 'employees.views.employee_pages', name ='employee_pages'),
#   url(r'^$','employees.views.index', name='index'),
#   url(r'newemployee', 'employees.views.newemployee', name='newemployee'),
#   url(r'newprospect', 'prospects.views.newprospects', name='newprospect'),  
# ]
