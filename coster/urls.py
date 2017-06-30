from django.conf.urls import url
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'coster'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index" ),
    url(r'^(?P<pk>\d)/$', views.DetailView.as_view(), name='detail'),
    url(r'^api/$', views.RidesList.as_view(), name='api'),

]

# urlpatterns = format_suffix_patterns(urlpatterns)