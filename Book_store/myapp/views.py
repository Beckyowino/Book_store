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

