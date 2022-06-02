from django.urls import path
from . import views

app_name = "gitdown"
urlpatterns = [
    path("", views.index, name="index"),
    path("oauth", views.oauth, name="oauth"),
    path("callback", views.callback, name="callback"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("delete", views.delete, name="delete"),
    path("logout", views.logout, name="logout")
    
]
