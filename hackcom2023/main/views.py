from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import UserData, outstation

# Create your views here.
def landingPage(request):
    return render(request, 'landingPage.html')

def loginn(request):
    if request.method == 'POST':
        post = request.POST
        user = User.objects.get(username=post['email'])
        if user.check_password(post['pass']):
            #login user
            login(request, user)
            return redirect('/onboarding')
        else:
            return HttpResponse("Incorrect Password")
    else:        
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        post = request.POST
        fname = post['name'].split(' ')[0]
        lname = " ".join(post['name'].split(' ')[1:])
        user = User.objects.create_user(first_name=fname, last_name=lname, username=post['email'], email=post['email'], password=post['pass'])
        return redirect('/onboarding')
    
    return render(request, 'register.html')

def onboarding(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    if request.method == 'POST':
        post = request.POST
        user = request.user
        
    return render(request, 'onboarding.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    return render(request, 'dashboard.html')
    

def outstationn(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = outstation.objects.all()
    users = []
    newData =[]
    for i in data:
        if i.driver == 1:
            continue
        newData.append(i.__dict__)
        newData[-1]['user'] = User.objects.get(id=i.driver).__dict__
    print(newData)
    return render(request, 'outstation.html', {'data': newData, 'userss': users})

def create_outstation(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        post = request.POST
        user = request.user
        outstation.objects.create(start=post['start'], end=post['end'], time=post['time'], date=post['date'], price=post['price'], driver=user.id, phone=post['phone'])
        return redirect('/outstation')
    else:
        return render(request, 'createOutstation.html')
    
def ecoRoute(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'ecoRoute.html')

def logoutt(request):
    logout(request)
    return redirect('/login')

def EcoTransit(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'publicTransit.html')

def outstation_detail(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = outstation.objects.get(id=id)
    return render(request, 'outstation_detail.html', {'data': data})

def findPool(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'findPool.html')