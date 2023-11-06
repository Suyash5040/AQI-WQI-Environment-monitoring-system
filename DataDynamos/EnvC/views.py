from django.http import HttpResponseRedirect
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render

from EnvC.models import *
from .forms import *

import razorpay
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


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









def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return redirect('/signin')
        else:
            return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect('/signin')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        confpassword=request.POST['confirmpassword']
        if password==confpassword:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            login(request,user)
            return redirect('/')
        else:
            return redirect('/signup')
    else:
        return render(request,"signup.html")









                                                                                                                                                                    




            