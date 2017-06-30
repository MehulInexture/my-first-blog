from django.conf.urls import url, include
from django.contrib import admin
from . import views
from coster import views as cv


app_name = "tenantTuto"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>\d)$', cv.DetailView.as_view(), name = 'detail')
]
