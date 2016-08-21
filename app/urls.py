from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.sites),
    url(r'^sites$', views.sites),
    url(r'^sites/(?P<id>[0-9]+)', views.site_page),
    url(r'^summary$', views.summary_sums),
    url(r'^summary-average$', views.summary_averages),
]
