from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST, require_GET



class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_name = request.user.username
        else:
            user_name = "гость"

        context = {
            'title': 'main page',
            'user_name': user_name,
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        context = {
            'title': 'POST'
        }
        return render(request, "index.html", context=context)


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self,request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main")
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

