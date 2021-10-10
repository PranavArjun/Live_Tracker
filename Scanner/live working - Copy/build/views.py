from django.shortcuts import render, get_object_or_404

from .models import TrackerScanner

from .forms import ScannerForm

from .filters import TrackerScannerFilter

from django.utils.text import slugify



# Create your views here.

def index(request):

    return render(request ,'index.html')


def listt(request):

    scanners = TrackerScanner.objects.all()

    myFilter = TrackerScannerFilter(request.GET, queryset=scanners)

    scanners = myFilter.qs


    context = {

        'scanners' : scanners, 

        'myFilter' : myFilter


    }

    return render(request , 'home/listt.html', context)


def scanner(request):

    context ={}

    form = ScannerForm(request.POST or None)

    if form.is_valid():

        form.save()

        form = ScannerForm()

    else:

        def cleaned_data(self):

            data = self.cleaned_data['package_id']

            city = self.cleaned_data['city']

            if TrackerScanner.objects.filter(slug = data).exists():
                form.save(update_fields=['city'])
                raise ValidationError("This question already exist")
                
                #TrackerScanner.objects.filter(city).update(city)

                
       

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

    else:
        data = self.cleaned_data['package_id']

        city = self.cleaned_data['city']

        if TrackerScanner.objects.filter(slug = data).exists():
            def update_view(request, id):
                context ={}
                obj = get_object_or_404(TrackerScanner, id = data)
                # pass the object as instance in form

                form = ScannerForm(request.POST or None, instance = obj)
            

                # save the data from the form and

                # redirect to detail_view

                if form.is_valid():

                    form.save()

                   # return HttpResponseRedirect("/"+id)
            

                # add form dictionary to context

                context["form"] = form
            

                return render(request, "update.html", context) 
        

            

        context['form']= form

    return render(request, "home/scanner.html", context)
    
    
    

def adding(request):

    return render(request , 'home/adding.html')


def create_view(request):

    # dictionary for initial data with 

    # field names as keys
    

    package_id, city = TrackerScanner.objects.get_or_create(name='')

    # add the dictionary during initialization

    form = ScannerForm(request.POST or None)

    if form.is_valid():

        form.save()

    else:

        form.save(update_fields=['city'])   
          

    context['form']= form


    return render(request, "home/scanner.html", context)

    return render(request, "home/scanner2.html", context)


# update view for details

def update_view(request, id):

    # dictionary for initial data with

    # field names as keys

    context ={}
 

    # fetch the object related to passed id

    obj = get_object_or_404(TrackerScanner, id = id)
 

    # pass the object as instance in form

    form = ScannerForm(request.POST or None, instance = obj)
 

    # save the data from the form and

    # redirect to detail_view

    if form.is_valid():

        form.save()

        return HttpResponseRedirect("/"+id)
 

    # add form dictionary to context

    context["form"] = form
 

    return render(request, "update_view.html", context)




