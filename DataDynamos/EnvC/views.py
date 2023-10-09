from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from EnvC.models import userfeed
from .forms import user
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

def industry(request):
    context = {'page': 'Industry Page'}
    return render(request, "industry.html", context )



def feedback(request): 
    #if request.POST:
    form=user(request.POST)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'feedback.html', {'form': form})  
    

   



    


def About(request):
    context = {'page': 'About'}
    return render(request, "About.html", context)










                                                                                                                                                                    