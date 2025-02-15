from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

User = get_user_model()

def UserLogin(request):
    if request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
        except Exception as e:
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url="login")
def UserLogout(request):
    logout(request)
    return redirect('login')
