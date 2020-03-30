from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views.token import CustomAuthToken
from .views.company import CompanyViewSet
from .views.user import UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'companies', CompanyViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('login/', CustomAuthToken.as_view()),
    url('user-info/', UserViewSet.as_view({ 'get': 'retrieve' })),
    url('signup/', UserViewSet.as_view({ 'post': 'create' })),
]
