from django.shortcuts import render, get_object_or_404
from .models import TrackerScanner
from .forms import ScannerForm


# Create your views here.
def index(request):
    return render(request ,'index.html')



def scanner(request):
    context ={}
  
    # add the dictionary during initialization
    form = ScannerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ScannerForm()
    
          
    context['form']= form
    return render(request, "home/scanner.html", context)

    #return render(request , 'home/scanner.html')
def scanner2(request):
    context ={}
    # add the dictionary during initialization
    form = ScannerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ScannerForm()
          
    context['form']= form
    return render(request, "home/scanner2.html", context)
    
    








