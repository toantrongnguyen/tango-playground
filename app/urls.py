from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views.company import CompanyViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'companies', CompanyViewSet)

urlpatterns = router.urls
