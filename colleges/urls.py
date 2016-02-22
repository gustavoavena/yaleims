from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.college_homepage, name='college_homepage'),
]


