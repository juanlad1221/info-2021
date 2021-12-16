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
        print(type(email))

        if str(email) == 'NoneType':
            email = User.email
            print('entro')

        #Comments.objects.create(newComment)

        return render(request, 'home.html')