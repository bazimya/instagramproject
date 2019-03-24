from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def welcome(request):

    
    return render(request, 'welcome.html')
def details (request,user_id):

    return HttpResponse('<h1>welcome home </h1>')