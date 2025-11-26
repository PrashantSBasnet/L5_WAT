import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

#
# '''you can get an http response'''
# def home(request):
#     return HttpResponse("Hello, World!")

'''you can render an html page'''
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.date.today()})

@login_required (login_url="/admin") #to block the access if the user is not logged in, add the decorator
def authorized(request):
    return render(request, 'home/authorized.html', {})