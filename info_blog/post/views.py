from django import contrib
from django.shortcuts import render

from comments.models import Comments
from .models import Post
from comments.forms import CommentForm

# Create your views here.
def allPost(request):
    #se obtiene todos los post
    result = Post.objects.all()
    
    #se obtiene una lista de diccionarios con el idpost y la cantidad de comments
    arr = []
    for i in result:
        nro_comment = Comments.objects.raw('SELECT * FROM post_post P JOIN comments_comments C WHERE P.id = C.post_id_id AND C.active = P.active AND C.post_id_id = %s',[i.id])
        arr.append({
            'id_post':i.id,
            'nro_comments':len(nro_comment)
        })
    
    context = {
        'data':result,
        'comments':arr
    }
    
    if request.user.id is None:
        context['form'] = CommentForm()
    else:
        context['form'] = CommentForm(instance=request.user)
        
    return render(request, 'home.html', context)

