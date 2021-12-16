from django.shortcuts import render
from .models import Post, models


# Create your views here.
def allPost(request):
    result = Post.objects.raw('SELECT * FROM post_post')
    print(result)
    return render(request, 'home.html',{'allPost':result})

