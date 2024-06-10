"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views
from myapp.views import ContactViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

