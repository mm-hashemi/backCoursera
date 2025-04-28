
from django.urls import path
from .views import (
    RegisterViews,
    LoginView,
    UserListView
   
)

urlpatterns = [
    path('signup/', RegisterViews.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
]
