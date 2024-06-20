"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('employee/', include('employee.urls')),
    path('department/', include('department.urls')),
    path('section/', include('section.urls')),
    path('payroll/', include('payroll.urls')),
    path('bank/', include('bank.urls')),
    path('gender/', include('gender.urls')),
    path('region/', include('region.urls')),
    path('jobtitle/', include('jobtitle.urls')),
    path('maritalstatus/', include('maritalstatus.urls')),
    path('militarystatus/', include('militarystatus.urls')),
    path('team/', include('team.urls')),
    path('costcenter/', include('costcenter.urls')),
    path('education/', include('education.urls')),
    path('college/', include('college.urls')),
    path('specialty/', include('specialty.urls')),
    path('gov/', include('gov.urls')),
    path('city/', include('city.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#