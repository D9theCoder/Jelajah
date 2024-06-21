from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World, I'm home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("I'm the about page")
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')

def profile(request):
    return render(request, 'profile.html')

