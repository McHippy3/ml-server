from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse('Welcome to the ML Server')