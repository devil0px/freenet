import time
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView

User = get_user_model()


# Create your views here.

def signup(request):
    if request.method == "GET":
        return render(request, 'users/signup.html')
    if request.method == "POST":
        email = request.POST['email']
        last_name = request.POST['lastname']
        frist_name = request.POST['firstname']
        password = request.POST['password']
        password2 = request.POST['password-repeat']
        user = request.POST['username']
        if password == password2:
            if user is not None:
                try:
                    user = User.objects.create_user(user, email, password)
                    # user = User.objects.create_user( email,last_name,first_name,user, password)
                    user.last_name = last_name
                    user.first_name = frist_name
                    user.save()
                    print(user)
                    messages.success(request, "Account Created Successfully You Can Login Now :D")
                    return render(request, 'users/signup.html')

                except:
                    messages.warning(request, "User Is Taken Try Another User !")
                    return render(request, 'users/signup.html')

        else:
            # messages
            messages.info(request, "Password Not Same !")
            return render(request, 'users/signup.html')


    return redirect('login')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Your account is disabled!")

        else:
            messages.add_message(request,30, "The username or password are not valid!")

    return render(request, 'users/login.html')


class Loguot(LogoutView):
    content_type = None
    extra_context = None
    http_method_names = ['get', 'post']
    next_page = "home"
    success_url_allowed_hosts = set('home')
