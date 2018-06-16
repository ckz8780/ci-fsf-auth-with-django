from django.shortcuts import render

def index(request):
    '''Return the index template'''
    return render(request, 'index.html')