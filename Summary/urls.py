"""Summary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from publicapp.views import *
from adminapp.views import *
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #Admin section
    url(r'^index/$',index,name='index'),
    url(r'^view_user/$',view_user,name='view_user'),
    url(r'^approve/(?P<id>[0-9]+)',approve,name='approve'),
    url(r'^view_auser/$',view_auser,name='view_auser'),
    url(r'^delete/(?P<id>[0-9]+)',delete,name='delete'),
    url(r'^view_search/$',view_search,name='view_search'),
    url(r'^view_contact/$',view_contact,name='view_contact'),

    #Public section
    url(r'^$',home,name='home'),
    url(r'^about/$',about,name='about'),
    url(r'^service/$',service,name='service'),
    url(r'^register/$',register,name='register'),
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^success/$',success,name='success'),
    url(r'^csuccess/$',csuccess,name='csuccess'),
    url(r'^error/$',error,name='error'),

    #User section
    url(r'^profile/$',profile,name='profile'),
    url(r'^edit/(?P<id>[0-9]+)',edit,name='edit'),
    url(r'^search/$',search,name='search'),
    url(r'^sum/$',sum,name='sum'),
    url(r'^result/$',result,name='result'),
    url(r'^fsum/$',fsum,name='fsum'),
    url(r'^fresult/$',fresult,name='fresult'),
    url(r'^ferror/$',ferror,name='ferror'),
    url(r'^wsum/$',wsum,name='wsum'),
    url(r'^wresult/$',wresult,name='wresult'),
    url(r'^ucontact/$',ucontact,name='ucontact'),
    url(r'^usuccess/$',usuccess,name='usuccess'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)