from django.conf.urls import url, include
from django.contrib import admin
# from coster import views as cv



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tenantTuto/', include('tenantTuto.urls')),
    # url(r'^coster/(?P<pk>\d)/$', cv.DetailView.as_view(), name = 'detail')
]
