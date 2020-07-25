from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        password = request.POST['pass']
        repass = request.POST['repass']
        if password == repass:
            if User.objects.filter(username=user_name).exists():
                print('User Name taken')
            elif User.objects.filter(email=email).exists():
                print('Email is taken')
            else:
                user = User.objects.create_user(username=user_name, password=password, email=email, first_name=first_name,
                                                last_name=last_name)
                user.save();
                print('Successfully created')
                return redirect('login')
        else:
            print('user not created')

    else:
        return render(request, 'reg.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['pass']
        user=auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credintials')
            return redirect('login')
    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')