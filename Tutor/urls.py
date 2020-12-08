from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^tutor/(\d+)',views.tutor,name ='tutor'),
    url(r'^location/',views.location,name ='location'),
    url(r'^name/',views.name,name ='name'),
    url(r'^experience/',views.experience,name ='experience')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)