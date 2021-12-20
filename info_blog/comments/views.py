from django.shortcuts import render
from .models import Comments, models
from django.contrib.auth.models import User

# Create your views here.
def showFormComments(request):
    return render(request, 'comments.html')


def saveComent(request, id):
    if request.method == "POST":
        newComment = request.POST.get("text-comment")
        email = request.POST.get('e-mail')
        post_id = id
    
        Comments.create(newComment, email, post_id)

        return render(request, 'home.html')