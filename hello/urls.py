from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("log/", views.log_message, name="log"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]