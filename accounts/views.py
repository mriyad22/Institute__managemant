from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def loginview(request):
    form_data  = AuthenticationForm()
    if request.method == "POST":
        form_data = AuthenticationForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user:
                login(request, user)
                messages.success(request, "You are Loged in")
                return redirect("dashboard")
        messages.warning(request, 'Invalid Credentials')

    form_data = AuthenticationForm()
    con = {
        "data" : form_data,
        "title" : "Login page",
        "btn" : "Login"
    }
    return render(request, "form.html", con)

@login_required
def logoutview(request):
    logout(request)

    return redirect("login_page")



def dashboardveiew(request):

    return render(request, "dasboard.html")