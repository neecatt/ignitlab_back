from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

"""
@param: router
@type: routers.DefaultRouter
@description: This is the router for the API
"""

router = routers.DefaultRouter()
router.register(r'startup', StartupViewSet)
router.register(r'investor', InvestorViewSet)
router.register(r'member', MemberViewSet)
router.register(r'faq', FAQViewSet)

"""
@param: urlpatterns
@type: list
@description: This is the list of urls for the API
"""
urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
