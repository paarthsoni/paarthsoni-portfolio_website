from django.shortcuts import render, HttpResponse, redirect
from Portfolio.models import viewersmessage
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        usermessage = viewersmessage(
            name=name, email=email, subject=subject, message=message)
        usermessage.save()
        messages.success(request, 'Message Sent Successfully to Paarth Soni!!')
        return redirect('/')

    return render(request, "index.html")
