from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

@login_required
def home(request):
    return render(request, "login.html", {})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def home(request):
    if request.method == 'POST':
        # Handle the screenshot uploads for each app
        if request.FILES.get('screenshot_whatsapp'):
            # Handle WhatsApp screenshot upload
            pass  # Your logic for WhatsApp upload

        if request.FILES.get('screenshot_instagram'):
            # Handle Instagram screenshot upload
            pass  # Your logic for Instagram upload

        if request.FILES.get('screenshot_facebook'):
            # Handle Facebook screenshot upload
            pass  # Your logic for Facebook upload

        return redirect('home')  # Redirect back to the home page after upload

    return render(request, 'home.html')


def upload_screenshot():
    return None