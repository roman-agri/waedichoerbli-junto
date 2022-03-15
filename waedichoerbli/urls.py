"""waedichoerbli URL Configuration

The `urlpatterns` list routes URLs to views.
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path, path

import juntagrico

from waedichoerbli import views as waedichoerbli

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^impersonate/', include('impersonate.urls')),
    re_path(r'^', include('juntagrico.urls')),
    re_path(r'^$', juntagrico.views.home),
    re_path(r'^', include('juntagrico_assignment_request.urls')),
    
    # special work areas
    path('my/specialwork', waedichoerbli.special_work_areas, name='special-work-areas'),

    # download area
    path('my/downloadarea', waedichoerbli.download_area, name='download-area'),

    # depot list management
    path('my/pdf/manage', waedichoerbli.list_mgmt, name='lists-mgmt'),
    path('my/pdf/manage/success', waedichoerbli.list_mgmt, {'success': True}, name='lists-mgmt-success'),
    path('my/pdf/manage/generate', waedichoerbli.list_generate, name='lists-generate'),
    path('my/pdf/manage/generate/future', waedichoerbli.list_generate, {'future': True}, name='lists-generate-future'),
    
]    


