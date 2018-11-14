from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def index_page(request):
    return render(request,'index.html')

def users_page(request):

    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return index_page(request)
    return render(request,'users.html',{"form":form})
    