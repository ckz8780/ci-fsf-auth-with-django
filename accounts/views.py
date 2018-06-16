from django.shortcuts import render, redirect, reverse
from django.contrib import auth

def index(request):
    '''Return the index template'''
    return render(request, 'index.html')
    
def logout(request):
    '''Log the user out'''
    auth.logout(request)
    return redirect(reverse('index'))