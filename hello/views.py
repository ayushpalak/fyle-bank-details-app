from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.filter().values()
    print(greetings)

    return JsonResponse({"greetings": list(greetings)},safe=False)
