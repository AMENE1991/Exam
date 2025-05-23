"""
URL configuration for Exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from AutoRu.views import VehicleViewSet, VehicleCreateView, VehicleDetailView, VehicleUpdateView, VehicleDeleteView, VehicleListView
from AuthApp.views import HomeView, RegisterView, LoginView, LogoutView

router = DefaultRouter()
router.register("Vehicles", VehicleViewSet, basename="viewsetVehicle")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('router', include(router.urls), name="router"),
    path('', HomeView.as_view(), name="main"),
    path('create/', VehicleCreateView.as_view(), name="create"),
    path('Foods/details/<int:pk>', VehicleDetailView.as_view(), name="details"),
    path('Foods/details/<int:pk>/update', VehicleUpdateView.as_view(), name="update"),
    path('Foods/details/<int:pk>/delete', VehicleDeleteView.as_view(), name="delete"),
    path('Vehicle/', VehicleListView.as_view(), name="Vehicles"),

    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
