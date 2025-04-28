from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import  CourseViewSet,HeroBannerView,CompaniesLogoView,CourseListView,PurchaseView

router=DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')# router.register(r'banner',HeroBannerView )
# router.register(r'company',CompaniesLogoView )
router.register(r'hero-banner', HeroBannerView, basename='hero-banner')
router.register(r'companies-logo', CompaniesLogoView, basename='companies-logo')
router.register(r'purchase', PurchaseView, basename='purchase')


urlpatterns = [
    path('', include(router.urls)),
    
    # path('roles/<int:course_id>/buy/', CourseViewSet.as_view({'post': 'buy_course'}), name='buy_course'),
    path('courseslist/', CourseListView.as_view(), name='course-list'),
     
]