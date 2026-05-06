from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("experiencia/", views.experience, name="experience"),
    path("experiencia/<slug:slug>/", views.experience_detail, name="experience_detail"),
    path("proyectos/", views.projects, name="projects"),
    path("stack/", views.stack, name="stack"),
    path("contacto/", views.contact, name="contact"),
]
