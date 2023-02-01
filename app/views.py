from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


class Landing(View):
    def get(self, request):
        return render(request, "landing.html")

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re-password")
        
        if password == re_password:
            user = User()
            user.first_name = fname
            user.last_name = lname
            user.username = username
            user.email = email
            user.set_password(password)
            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            user.save()

            login(request, user)
            return redirect("dashboard")

        return redirect("landing-page")


class LogIn(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")

        return redirect("landing-page")
    

class Dashboard(View):
    def get(self, request):
        return render(request, "dashboard.html")