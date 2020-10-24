from django.shortcuts import render
from django.http import HttpResponse
from .models import Test1

# Create your views here.
def index(request):
    data = Test1.objects.all()
    params = {
        'data':data,
    }
    return render(request,'hello/index.html',params)