from django.shortcuts import render

# Create your views here.
def ods17(request):
    return render(request, 'ods17.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')