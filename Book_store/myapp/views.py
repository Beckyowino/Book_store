from django.shortcuts import render

# Create your views here.
def books(request):
    return render(request, 'books.html')

def pricing(request):
    return render(request, 'pricing.html')

def authors(request):
    return render(request, 'authors.html')

def events(request):
    return render(request, 'events.html')

def stefan(request):
    return render(request, 'stefan.html')

def virginie(request):
    return render(request, 'virginie.html')

def leo(request):
    return render(request, 'leo.html')

def bram(request):
    return render(request, 'bram.html')

def michelle(request):
    return render(request, 'michelle.html')

def virginia(request):
    return render(request, 'virginia.html')

def charles(request):
    return render(request, 'charles.html')

def kurt(request):
    return render(request, 'kurt.html')

def markus(request):
    return render(request, 'markus.html')

