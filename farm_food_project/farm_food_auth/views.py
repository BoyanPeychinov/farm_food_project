from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from farm_food_project.farm_food_auth.forms import SignUpForm, SignInForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'auth/sign_up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm
    success_url = reverse_lazy('index')


def sign_out(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, 'index.html')