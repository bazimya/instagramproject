from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Album,user


def welcome (request):
    album  = Album.objects.all()
   
    avata  = user.objects.all()
    userd=None
    
    for imagesd in avata:
        userd=imagesd
    getuse={'name':album}
    prifiles={'user':userd}

    return render(request,'index.html',{'user':userd,'name':album})
def details (request,user_id):
        try:
            album = Album.objects.get(pk=user_id)
        except Album.DowsNoteExist:
            raise Http404('user nta wurimo muri database')
        return render(request,'welcome.html',{'bazimy':album})
def allimages(request):
    return render(request,'allimages.html')