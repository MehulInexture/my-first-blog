from django.conf.urls import url
from coster import views

urlpatterns = [
    url(r'^api/$', views.RidesList.as_view(), name="api" ),
]