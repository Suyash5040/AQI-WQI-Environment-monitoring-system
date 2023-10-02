from multiprocessing import context
from django.shortcuts import render

from EnvC.form import feedbackForm

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

def feedback(request):  # sourcery skip: remove-pass-body
    if request.method=='POST':
        pass
    else:
        form=feedbackForm()
    context = {'page': 'Feedback page'}
    return render(request, "feedback.html", {'form':form} )

def About(request):
    context = {'page': 'About'}
    return render(request, "About.html", context)



                                                                                                                                                                    