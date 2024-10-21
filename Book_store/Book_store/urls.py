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
from myapp.views import fetch_events, books, authors, pricing 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books, name='books'),
    path('events/', fetch_events, name='events'),
    path('authors/', authors, name='authors'),
    path('pricing/', pricing, name='pricing'),
    path('books/', books, name='books'),

]

