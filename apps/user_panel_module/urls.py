from django.urls import path
from . import views
app_name = "user_panel"
urlpatterns = [
    path('user-panel',views.UserPanelView.as_view(),name = "user-panel")
]