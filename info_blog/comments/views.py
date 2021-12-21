from django import forms
from django.shortcuts import redirect, render , get_object_or_404
from .models import Comments
from post.models import Post
from django.contrib.auth.models import User
from .forms import CommentForm, newCommentForm, editCommentForm

# Create your views here.
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


def comments(request):
    #obtengo el usuario
    id_user = request.user.id
    
    #obtengo los comentarios segun el usuario
    result = Comments.objects.raw('SELECT * FROM comments_comments C JOIN post_post P WHERE C.post_id_id = P.id AND C.active = P.active AND P.user_id_id = %s',[id_user])
    datos = {}
    datos['user'] = request.user
    arr = []
    
    for i in result:
       arr.append({
           'id':i.id,
           'post_title':i.title,
           'comment':i.comment,
           'mail':i.email,
           'time':i.created
       })
    datos['comments'] = arr
    
    context = {'data':datos}
    
    return render(request, 'admin2-comments.html', context)


def oneComment(request, id):
    result = Comments.objects.get(id=id)
    context = {'data':result}
    return render(request, 'admin2-oneComment.html',context)


def _admin2deleteComment(request,id):
    #obtengo instancia de la busqueda por id
    result = get_object_or_404(Comments, id = id)
    #si es positiva
    if result:
        #elimino el post
        result.delete()
        return redirect('comments')
    else:
        #envio a pag. de error
        pass


def _admin2NewComment(request):
    #creo el context con el form y sus datos p/editar
    context = {'form':newCommentForm()}

    #si la peticion es post
    if request.method == "POST":
        formulario = newCommentForm(data=request.POST)

        if formulario.is_valid:
            #grabo el form y envio msg
            formulario.save()
            return redirect('comments')
        else:
            #envio el form de nuevo
            context['form'] = formulario
    return render(request, 'admin2-comment-new.html', context)


def admin2EditComment(request,id):
    #obtengo el elemento buscado por id
    result = get_object_or_404(Comments, id = id)
    
    #si obtiene resultado
    if result:
        #creo el context con el form y sus datos p/editar
        context = {'form':editCommentForm(instance=result)}
    else:
        context = editCommentForm()

    #si la peticion es post
    if request.method == "POST":
        #le paso al form la peticion con los datos y la busqueda por id
        formulario = editCommentForm(data=request.POST, instance=result)

        #verifica los datos del form
        if formulario.is_valid:
            #graba el nuevo form
            formulario.save()
            return redirect('comments')
        #si no es valido devuelve el form
        context['form']=formulario
        
    return render(request, 'admin2-comment-edit.html',context)


