from django.contrib.messages.api import error
from django.db.models.expressions import F
from django.http import response
from django.shortcuts import render , HttpResponse
from home.models import Contact , TrackerScanner
from django.contrib import messages


import json

# Create your views here.

def home(request):
    if request.method=="POST":
        orderid = request.POST.get('Orderid', '')
        orderdate = request.POST.get('OrderDate', '')
        try :
            order = TrackerScanner.objects.filter(package_id=orderid , date=orderdate)
            if len(order)>0:
                gpslink = TrackerScanner.objects.filter(package_id= orderid)
                gpslinks = []
                for item in gpslink:
                    gpslinks.append({'char': item.gps_no_field})
                    response = json.dumps(gpslinks)
                return HttpResponse(response)

            else:
                return HttpResponse('{}')
        except Exception as e :
            return HttpResponse('{}')

    return render(request ,'home/home.html')









def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name , email , phone , content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name , email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent")

    return render(request ,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def services(request):
    return render(request,'home/services.html')


# def search(request):
#     if request.method == "GET":
#         orderid = request.GET['Orderid']
#         orderdate = request.GET['OrderDate']
        

                           
   