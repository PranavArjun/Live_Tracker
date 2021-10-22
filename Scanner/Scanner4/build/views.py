from django.shortcuts import render, get_object_or_404
from .models import TrackerScanner
from .forms import ScannerForm


# Create your views here.
def index(request):
    return render(request ,'index.html')



def scanner(request):
    context={

    }
    form = ScannerForm(request.POST or None)
    if (request.method=="POST"):
        obj , created = TrackerScanner.objects.get_or_create(package_id = request.POST.get("package_id"))
        obj.gps_no_field = request.POST.get("gps_no_field")
        
        obj.save()
    
          
    context['form']= form
    return render(request, "home/scanner.html", context)

    #return render(request , 'home/scanner.html')

    
    








