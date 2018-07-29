from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == "POST":
        # Check if passwords match
        if request.POST.get("password") == request.POST.get("confirm-password"):
            # Check if username exists in User.objects
            try:
                username = User.objects.get(username=request.POST["username"])
                error = "{} has already been taken".format(username)
                return render(request, "accounts/signup.html", {"error": error})

            # Authorize and create new user then redirect home
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password"]
                )
                login(request, user)
                return redirect("products:index")

        # Return error if passwords do not match
        else:
            error = "Passwords did not match"
            return render(request, "accounts/signup.html", {"error": error})
    else:
        # User has asked to sign up
        return render(request, "accounts/signup.html")


def login_view(request):
    # POST REQUEST
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("products:index")
        else:
            error = "username or password is incorrect"
            return render(request, "accounts/login.html", {"error": error})
    
    # OTHER HTTP REQUESTS
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("products:index")
