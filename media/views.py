from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Album,user
from .forms import  Formprofile


@login_required(login_url='/accounts/login/')
def welcome (request):
    
    userinformation = user.objects.all()
    image = None
    for img in userinformation:
        image = img.profile
        name =img.firstname
        print(name)
    return render(request, 'index.html',{"image":image,'name':name})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = Formprofile(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            article = form.save(commit=False)
            article.curentus = current_user
            article.save()
        return redirect('instagram')

    else:
        form = Formprofile() 
    return render(request, 'profile.html', {"form": form})
def details (request,user_id):
    try:
        album = Album.objects.get(pk=user_id)
    except Album.DowsNoteExist:
        raise Http404('user nta wurimo muri database')
    return render(request,'welcome.html',{'bazimy':album})
def allimages(request):
    return render(request,'allimages.html')

def update_profile(request, image_id):
    current_user = request.user
    image = str(image_id)
    if request.method == 'POST':
        form = Formprofile(request.POST, request.FILES)
        if form.is_valid():
            fname = form.cleaned_data['firstname']
            lname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            profile = form.cleaned_data['profile']
            
            # article = form.save(commit=False)
            # article.curentus = current_user
            user.update_user(image, fname, lname, profile,email)
        return redirect('instagram')

    else:
        form = Formprofile() 
    return render(request, 'update.html', {"form": form, 'image':image})
