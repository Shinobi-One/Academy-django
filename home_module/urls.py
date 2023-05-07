from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('about-us', views.AboutUs_View.as_view(), name='about-us-page'),
]
