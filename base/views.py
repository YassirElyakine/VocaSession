from django.shortcuts import render,redirect
from .models import Vocabulary
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout

def VocaSession(request):
    if request.user.is_superuser:
        return render(request,'base/VocaSession.html', {'vocabularies':Vocabulary.objects.all()})
    else:
        return redirect('/login/')

def add(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            for vocabulary in Vocabulary.objects.all():
                if vocabulary.title == request.POST.get('title'):
                    return HttpResponse('<h1>Another item with the same title already exists!</h1>')
            else:
                Vocabulary.objects.create(title=request.POST.get('title'),meaning=request.POST.get('meaning'))
                return render(request, 'base/add_vocabulary.html')
        else:
            return render(request, 'base/add_vocabulary.html')
    else:
        return redirect('/login/')

def edit(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            search_query = Vocabulary.objects.get(title=request.POST.get('title'))
            if request.POST.get('new_title') != '':
                search_query.title = request.POST.get('new_title')
            if request.POST.get('meaning') != '':
                search_query.meaning = request.POST.get('meaning')
            search_query.save()
            return render(request, 'base/edit_vocabulary.html')
        else:
            return render(request, 'base/edit_vocabulary.html')
    else:
        return redirect('/login/')

def delete(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            Vocabulary.objects.get(title=request.POST.get('title')).delete()
            return render(request, 'base/delete_vocabulary.html')
        else:
            return render(request, 'base/delete_vocabulary.html')
    else:
        return redirect('/login/')

def login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/')
    else:
        if request.method == 'POST':
            username,password = request.POST['username'],request.POST['password']
            account = authenticate(request,username=username,password=password)
            if account is not None and account.is_superuser:
                auth_login(request,account)
                return redirect('/')
            else:
                return HttpResponse('Information is invalid, and account does not exist.')
        else:
            return render(request, 'base/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/login/')