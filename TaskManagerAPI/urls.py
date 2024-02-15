from django.urls import path
from .import views

urlpatterns=[
    path("", views.create_user_view, name="create_user"),
    path("login/", views.login_view, name="login"),
    path("mylogin/", views.login_template, name="mylogin")
]