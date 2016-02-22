from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^input', views.input_scores, name='input_scores'),
    url(r'^remove', views.remove_scores, name='remove_scores'),
]


