"""
URL configuration for Book_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import events, books, authors, pricing, stefan, virginie, bram, charles, kurt, markus, michelle, virginia, leo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books, name='books'),
    path('events/', events, name='events'),
    path('authors/', authors, name='authors'),
    path('pricing/', pricing, name='pricing'),
    path('books/', books, name='books'),
    path('authors/stefan', stefan, name='stefan' ),
    path('authors/virginie', virginie, name='virginie' ),
    path('authors/leo', leo, name='leo' ),
    path('authors/bram', bram, name='bram' ),
    path('authors/charles', charles, name='charles' ),
    path('authors/kurt', kurt, name='kurt' ),
    path('authors/markus', markus, name='markus' ),
    path('authors/michelle', michelle, name='michelle' ),
    path('authors/virginia', virginia, name='virginia' ),
]

