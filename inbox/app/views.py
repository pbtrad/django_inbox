from tkinter.messagebox import RETRY
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def inbox(request):
    return render(request, "inbox.html")