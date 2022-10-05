from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('knu:home')
        else:
            messages.success(request, ("Du konntest nicht angemeldet werden"))
            return redirect('member:login')
    else:
        pass

    # Return an 'invalid login' error message.


        return render(request, 'authenticate/login.html', {})

# Create your views here.
