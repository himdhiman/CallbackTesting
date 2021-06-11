from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def getData(request):
    if(request.method == "POST"):
        print(request.POST)
        return HttpResponse("OK")


