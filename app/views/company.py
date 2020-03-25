from django.http import HttpResponse, JsonResponse
from django.views import View
from ..models import Company

class CompanyView(View):

    def get(self, request):
        return JsonResponse(list(Company.objects.values()), safe=False)
