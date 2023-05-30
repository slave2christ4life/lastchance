from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listings:index')
        else:
            # Return an 'invalid login' error message.
             return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('listings:index')  # Redirect to your desired page
    else:
        form = CustomUserCreationForm() 
    return render(request, 'users/register.html', {'form': form})
