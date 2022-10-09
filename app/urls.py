from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("new/", views.new_hn, name='new'),
    path("post/<pk>/", views.post, name='post'),
    path("ask-hn/", views.ask_hn, name='askhn'),
    path("show-hn/", views.show_hn, name='showhn'),
    path("hn/jobs/", views.jobs_hn, name='jobshn'),

]