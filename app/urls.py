from django.urls import path
from . import views
from .views.company import CompanyView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='company-index'),
]
