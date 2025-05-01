
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    RegisterViews,
    LoginView,
    UserListView,
    
)

urlpatterns = [
    path('signup/', RegisterViews.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    # path('update-profile/', ProfileImageUploadView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
