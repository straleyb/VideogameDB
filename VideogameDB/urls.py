from django.conf.urls import patterns, include, url
from django.contrib import admin
from VideogameDB import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vidya/', include('vidya.urls', namespace = "vidya")),
)
