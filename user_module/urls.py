from django.urls import path
from . import views

app_name= "user"
urlpatterns = [
    path('sign-up', views.RegisterView.as_view(), name='register'),
    path('forget_password/', views.ForgetPassword.as_view(), name='forget_password'),
    path('sign-in', views.LoginView.as_view(), name='login'),
    path('user-activation/<str:activation_code>',views.UserActivateView.as_view(),name= "user_activation"),
    path('reset_password/<str:active_code>',views.ResetPassword.as_view(),name= "reset-password"),

    ]