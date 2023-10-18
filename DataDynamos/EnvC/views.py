from django.http import HttpResponseRedirect
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render

from EnvC.models import *
from .forms import *

import razorpay
from django.views.decorators.csrf import csrf_exempt



def nav(request):
    context = {'page': 'nav'}
    return render(request, "nav.html", context)


def home(request):
    context = {'page': 'EnviroConnect'}
    return render(request, "home.html", context)

def AQI(request):
    context = {'page': 'AQI'}
    return render(request, "AQI.html", context)

def WQI(request):
    context = {'page': 'WQI'}
    return render(request, "WQI.html", context)

def Environment(request):
    context = {'page': 'Environment'}
    return render(request, "Environment.html", context)




def industry(request ):
    
    form2=indus(request.POST)
    if form2.is_valid():
        form2.save()
        return redirect(home)


    if request.method=='POST':
        client = razorpay.Client(auth=("rzp_test_4135eGDYhDKQzy", "QDUNleqh9rmUJtovo28tZgKG"))

        DATA = {                    
            "amount": 100,
            "currency": "INR",
            "receipt": "receipt#1",

                }
        payment = client.order.create({'amount': 'amount', 'currency': 'INR','payment_capture': '1'})


    else:
        form2 = indus()
        return render(request, 'industry.html', {'form2': form2}) 
            
        
    





def feedback(request): 
    #if request.POST:
    form=user(request.POST)
    if form.is_valid():
        form.save()
        return redirect(home)
    else:
        form = user()
        return render(request, 'feedback.html', {'form': form})
    
    
    
       

   

def About(request):
    context = {'page': 'About'}
    return render(request, "About.html", context)










                                                                                                                                                                    




            