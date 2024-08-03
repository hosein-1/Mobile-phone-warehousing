from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.http import HttpResponse

from .forms import LoginForm


def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('mobiles_list')

        
    
    else: 
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form}) 


def user_logout_view(request):
    logout(request)
    messages.success(request, 'خارج شدید.')
    return redirect('account:login')
    
    