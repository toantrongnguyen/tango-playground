from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.token import CustomAuthToken
from .views.company import CompanyViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'companies', CompanyViewSet)

urlpatterns = router.urls
urlpatterns += [
    url(r'^login/', CustomAuthToken.obtain_auth_token)
]
