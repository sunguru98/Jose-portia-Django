from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_page, name="index"),
    path("users/",views.users_page, name="users")
]