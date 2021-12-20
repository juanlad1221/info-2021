from django import forms
from django.shortcuts import redirect, render
from .models import Comments, models
from django.contrib.auth.models import User
from .forms import CommentForm

# Create your views here.
'''def saveComent(request, id):
    #verifica q la peticion sea post
    if request.method == "POST":
        #obtiene los datos a guardar de la peticion
        newComment = request.POST.get("text-comment")
        email = request.POST.get('e-mail')
        post_id = int(id)
        print(post_id)
        #usando metodo del modelo crea el post
        Comments.create(newComment, email, post_id)
        return redirect('home')'''
    
def saveComment(request):
    #verifica q la peticion sea post
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid:
            form.save()
            return render(request, 'home.html',{})
        else:
            form = CommentForm()
    else:
        pass


