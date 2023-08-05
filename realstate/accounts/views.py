from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordc = request.POST.get('password2')

        if password == passwordc:
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username already exixts")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email already exixts")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    messages.success(request, 'Registration successfull! You can now login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, "accounts/register.html")



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == 'POST':
        print("logout")
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    else:
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    return render(request, "accounts/dashboard.html", {'contacts' : user_contacts, "user": request.user})




