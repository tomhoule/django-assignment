from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.dummy_view),
    url(r'^sites', views.dummy_view),
    url(r'^summary', views.dummy_view),
]
