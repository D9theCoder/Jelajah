from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def fatahillah(request):
    return render(request, 'tour/fatahillah.html')

def bankindonesia(request):
    return render(request, 'tour/bankindonesia.html')

def mandiri(request):
    return render(request, 'tour/mandiri.html')

@login_required(login_url='/users/login/')
def virtual_fatahillah(request):
    return render(request, 'tour/virtual_fatahillah.html')

@login_required(login_url='/users/login/')
def virtual_bankindonesia(request):
    return render(request, 'tour/virtual_bankindonesia.html')

@login_required(login_url='/users/login/')
def virtual_mandiri(request):
    return render(request, 'tour/virtual_mandiri.html')
