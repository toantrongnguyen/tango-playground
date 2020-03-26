from django.urls import path
from . import views
from .views.company import company_collection, company_element

urlpatterns = [
    path('companies/', company_collection, name='company-index'),
    path('companies/<int:company_id>', company_element, name='company-index'),
]
