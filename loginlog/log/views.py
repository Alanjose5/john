from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def qwe(request):
    if request.method=='POST':
        username=request.POST['txt']
        password = request.POST['password']
        email = request.POST['email']
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.info(request,"Registration successful")
    return render(request,'index.html')
def login(request):
    if request.method == 'post':
        username=request.POST['txt']
        password=request.POST['password']
        email=request.POST['email']
        user = auth.authenticate(username=username,email=email,password=password)
        if user is not None:
            auth.login(request,user)
        else:
            messages.info(request,'invalid details')
    return render(request,'index.html')