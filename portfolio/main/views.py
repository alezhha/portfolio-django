from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import SendMessage

# Create your views here.

def index(request):
    return render(request, 'index.html')

def formMessage(request):
    if request.method == "POST":
        sendMessage = SendMessage()
        sendMessage.email = request.POST.get('email')
        sendMessage.phone_number = request.POST.get('phone_number')
        sendMessage.message = request.POST.get('message')
        sendMessage.save()
        return HttpResponseRedirect('/')