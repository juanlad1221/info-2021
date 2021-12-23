from django import contrib
from django.contrib import messages
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
from post import *
from post.models import Category, Post
from post.forms import Editform, Newform


#vistas de login
def showLogin(request):
    return render(request,'login.html')


def autenticate(request):
    #comprueba que la peticion sea post
    if request.method == "POST":
        #Obtengo de la peticion los valores
        username = request.POST.get("user")
        password = request.POST.get("password")
       
        #compruebo los datos en el modelo/BD
        user = authenticate(username=username, password=password)
        #Compruebo si el usuario es superuser
        result = User.objects.filter(username = username).filter(is_superuser = 1).exists()
        
        #si es usuario escritor 
        if user is not None and result == False:
            login(request, user)
            return redirect('home')
        #si es superuser
        elif user is not None and result:
            login(request, user)
            return redirect('_admin2')
        #si no cumple ninguna de ambas
        else:
            # Si no esta autorizado envia error
            messages.error(request, 'Error: Login failed...')
            return render(request, "home.html")

    
def home(request):
    result = Post.objects.all()
    context = {'data':result}
    return render(request, 'home.html', context) 


def logout_view(request):
    #Deslogea al usuario actual
    logout(request)
    return redirect('home')




#vistas de admin2
def showAdmin2(request):
    return render(request, 'admin2-home.html')


def showAdmin2Post(request):
    #Obtiene los post activos
    result = Post.objects.filter(active = 1)
    #si la consulta fue exitosa
    if result:
        context = {'data':result}
    else:
        #si la consulta NO fue exitosa
        context = {}
    return render(request, 'admin2-post.html', context)


def showAdmin2EditPost(request, id):
    #obtengo el post buscado por id
    result = get_object_or_404(Post, id = id)
    
    #si obtiene resultado
    if result:
        #creo el context con el form y sus datos p/editar
        context = {'form':Editform(instance=result)}
    else:
        context = {}

    #si la peticion es post
    if request.method == "POST":
        print(request.POST)
        #le paso al form la peticion con los datos y la busqueda por id
        formulario = Editform(data=request.POST, instance=result)
        #verifica los datos del form
        if formulario.is_valid:
            #graba el nuevo form
            formulario.save()
            return redirect('_admin2-post')
        #si no es valido devuelve el form
        context['form']=formulario

    return render(request, 'admin2-post-edit.html', context)


def admin2DeletePost(request, id):
    #obtengo instancia de la busqueda por id
    result = get_object_or_404(Post, id = id)
    #si es positiva
    if result:
        #elimino el post
        result.delete()
        return redirect('_admin2-post')
    else:
        #envio a pag. de error
        pass 


def admin2NewPost(request):
    #creo el context con el form y sus datos p/editar
    context = {'form':Newform(initial={'user_id':request.user})}
    
    #si la peticion es post
    if request.method == "POST":
        formulario = Newform(data=request.POST)
        
        if formulario.is_valid:
             #grabo el form 
            post_ = formulario.save(commit=False)
            #incorporo el user
            post_.user_id = request.user
            #grabo nuevamente
            post_.save()
            return redirect('_admin2-post')
        else:
            #envio el form de nuevo
            context['form'] = formulario

    return render(request, 'admin2-post-new.html', context)


def admin2Search(request):
    select = Category.objects.all()
    context = {
        'select':select,
        'table':False
    }
    return render(request, 'admin2-search.html', context)


'''def admin2SearchMes(request):
    select = Category.objects.all()
    datos = Post.objects.raw("SELECT * from post_post WHERE created BETWEEN '2021-12-01' and '2021-12-31'")
    


    context = {
        'select':select,
        'table':datos
    }

    if request.POST:
        #print(request.POST['select-mes'])
        return render(request, 'admin2-search.html', context)


def admin2SearchCategory(request):
    select = Category.objects.all()
    context = {
        'select':select,
        
    }

    if request.POST:
        print(request.POST['select-category'])
        return render(request, 'admin2-search.html', context)
'''
