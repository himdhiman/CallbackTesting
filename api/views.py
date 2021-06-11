from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def getData(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode())
        print(data)
        return HttpResponse("This is a bot")


