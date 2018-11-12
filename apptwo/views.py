from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import User
# Create your views here.

def index_page(request):
    return render(request,'index.html')

def users_page(request):
    user_details = {"users":User.objects.order_by("first_name")}
    return render(request,'users.html',context=user_details)