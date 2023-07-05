from django.urls import path
from . import views
app_name = "user_panel"
urlpatterns = [
    path('user',views.UserPanelView.as_view(),name = "user-panel"),
    path('user/edit-user-password', views.EditPasswordView.as_view(),name="edit-user-password"),
    path('user/edit-user-panel', views.EditUserPanelView.as_view(),name="edit-user-panel")
]