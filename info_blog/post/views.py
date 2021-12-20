from django.shortcuts import render
from .models import Post


# Create your views here.
def allPost(request):
    result = Post.objects.all()
    return render(request, 'home.html',{'data':result})

