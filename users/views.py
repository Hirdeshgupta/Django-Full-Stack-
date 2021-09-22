from typing import Pattern
from django.shortcuts import render, redirect
from .form import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account is Successfully created please log in !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Sucessfullly Updated Profile !')
            redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})
# Create your views here.
