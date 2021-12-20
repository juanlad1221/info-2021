from django import contrib
from django.shortcuts import render
from .models import Post
from comments.forms import CommentForm

# Create your views here.
def allPost(request):
    result = Post.objects.all()
    context = {
        'data':result
    }
    print(type(request.user.id))
    if request.user.id is None:
        context['form'] = CommentForm()
    else:
        context['form'] = CommentForm(instance=request.user)
        
    return render(request, 'home.html', context)

