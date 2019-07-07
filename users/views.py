from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.shortcuts import render, redirect

from blog.models import BlogPost
from .forms import UserRegisterForm, ProfileForm
from .models import Profile


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Log In'
    }


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            username = instance.username
            instance.save()
            messages.success(request, f'Account for {username} was created succesfully. You may now log in.')
            return redirect('home')
    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    user = User.objects.get(username=request.user.username)
    objects = BlogPost.objects.filter(author=user)
    context = {
        'title': 'Profile',
        'user': user,
        'objects': objects
    }
    return render(request, 'users/profile.html', context)


@login_required
def update_profile(request):
    instance = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=instance)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile Picture Updated")
            return redirect('profile')
    context = {
        'title': 'Update Profile Picture',
        'form': form
    }
    return render(request, 'users/update_pp.html', context)


@login_required
def user_specific(request, username):
    spec_user = User.objects.get(username=username)
    objects = BlogPost.objects.filter(author=spec_user)
    context = {
        'spec_user': spec_user,
        'objects': objects
    }
    return render(request, 'users/specific.html', context)


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = '/users/password_change_done/'
    extra_context = {
        'title': 'Password Change',
    }


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'
    extra_context = {
        'title': 'Passwword Change Done'
    }


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = '/users/password_reset_done/'
    extra_context = {
        'title': 'Password Reset',
    }


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    extra_context = {
        'title': 'Password Reset Done',
    }


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = '/users/password_reset_complete/'
    extra_context = {
        'title': 'Password Reset Confirm'
    }


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
    extra_context = {
        'title': 'Password Reset Done'
    }
