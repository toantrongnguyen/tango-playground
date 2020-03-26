from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from ..models import Company

def index(request):
    return JsonResponse(list(Company.objects.values()), safe=False)

def store(request):
    return JsonResponse(list(Company.objects.values()), safe=False)

def company_collection(request):
    if request.method == 'GET':
        return index(request)
    elif request.method == 'POST':
        return index(request)

    raise Http404()

def company_element(request):
    if request.method == 'GET':
        return index(request)
    # elif request.method == 'post':
        # return index(request)

    return Http404()

def show(request, company_id):
    return JsonResponse(Company.objects.values().get(pk=company_id), safe=False)
