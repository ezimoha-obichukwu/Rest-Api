from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home_page, name="api-home-page")
]