from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ReservetionForm
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World")

class HelloBrazil(View):
    def get(self , request):
        return HttpResponse("Hello Brazil")

def home(request):
    form = ReservetionForm()

    if request.method =='POST':
        form = ReservetionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Sucess")

    return render(request, 'index.html', { 'form':form })