from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render

from EnvC.models import *
from .forms import *

import razorpay
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required




@login_required(login_url='login')

#navbar
def nav(request):
    context = {'page': 'nav'}
    return render(request, "nav.html", context)

#home page
def home(request):
    context = {'page': 'EnviroConnect'}
    return render(request, "home.html", context)

#Air quality index page
def AQI(request):
    context = {'page': 'AQI'}
    return render(request, "AQI.html", context)

#Water quality index page
def WQI(request):
    context = {'page': 'WQI'}
    return render(request, "WQI.html", context)

#Environnment page
def Environment(request):
    context = {'page': 'Environment'}
    return render(request, "Environment.html", context)



#suggestion page for industries
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
            
        
    



#feedback page
def feedback(request): 
    #if request.POST:
    form=user(request.POST)
    if form.is_valid():
        form.save()
        return redirect(home)
    else:
        form = user()
        return render(request, 'feedback.html', {'form': form})
    
    
    
       

   
#About page
def About(request):
    context = {'page': 'About'}
    return render(request, "About.html", context)






#signup page
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/login/')
    
    return render (request,'signup.html')



#login page
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
           
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')



#logout page
def logout(request):
    logout(request)
    return redirect('login')









                                                                                                                                                                    




            