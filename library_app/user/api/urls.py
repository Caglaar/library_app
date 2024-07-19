from django.urls import path
from user.api import views as api_view


urlpatterns = [
    path('users/', api_view.users_list_api_view.as_view(), name="users-list"),
    path('users/<int:pk>', api_view.users_detail_api_view.as_view(), name="user-detail"),
]
