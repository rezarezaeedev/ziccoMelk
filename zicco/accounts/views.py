from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'cp/dashboard.html')
    
    
def login(request):
    if request.method == 'POST':
        username,password   =   request.POST['username'], request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('indexPage')
    else:
        return redirect('indexPage')

def register(request):
        if request.method == 'POST':
            email   =   request.POST['email']
            username   =   request.POST['username']
            password   =   request.POST['password']
            repassword   =   request.POST['repassword']
            if  len(password) < 8  :
                return redirect('indexPage')
            else:
                if password != repassword:
                    return redirect('indexPage')
                else:
                    if User.objects.filter(username=username).exists():
                        return redirect('indexPage')
                    else:
                        if User.objects.filter(email=email).exists():
                            return redirect('indexPage')
                        else:
                            user = User.objects.create_user(username=username, email=email, password=password)
                            user.save()
                            user = auth.authenticate(username=username, password=password)
                            if user is not None:
                                auth.login(request, user)
                                return redirect('dashboard')

        else:
                return redirect('indexPage')
    
    

    