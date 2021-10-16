from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthenticationView.as_view(), name="logIn"),
    path('auth/', views.RoleUser.as_view(), name="roleUser"),
    path('logout/', views.LogoutView.as_view(), name='logout')]
