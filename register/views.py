from django.shortcuts import render, redirect
from . import forms

def register(request):
    if request.method == "POST":
        form = forms.register_form(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = forms.register_form()

    return render(request, 'register/register.html', {"form":form})

