from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import  RoleViewSet,BannerViewSet,CompanyViewSet

router=DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'banner',BannerViewSet )
router.register(r'company',CompanyViewSet )


urlpatterns = [
        path('', include(router.urls)),
]
