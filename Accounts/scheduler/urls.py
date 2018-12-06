from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    url(r'^login', views.login, name='chalk_login'),
    url(r'^schedule', views.schedule, name='chalk_schedule'),
    url(r'^entry', views.new_entries, name='chalk_entry'),
    url(r'^logout', LogoutView, {
        'next_page': '/login'
    }),
    url(r'^about', views.about, name='chalk_about'),
    url(r'^contact', views.contact, name='chalk_contact'),
    url(r'^', views.home, name='chalk_home'),
]