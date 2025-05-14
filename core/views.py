from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Blog
# Create your views here.
def home_view(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'blogs': blogs})