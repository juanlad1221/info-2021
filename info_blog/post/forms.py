
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django.forms import fields
from .models import Category, Post

class Editform(ModelForm):

    title = forms.CharField(label='TITLE',widget=forms.TextInput(attrs={'class':'form-control mb-4'}))
    created = forms.CharField(label='CREATED', widget=forms.TextInput(attrs={'class':'form-control mb-4'}))
    category_id = forms.ModelChoiceField(label='CATEGORY', queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control mb-4'}))
    content = forms.CharField(label='POST', widget=forms.Textarea(attrs={'class':'form-control'}))
        
    class Meta:
        model = Post
        fields = ['title','created','category_id','content']

class Newform(ModelForm):
    title = forms.CharField(label='TITLE',widget=forms.TextInput(attrs={'class':'form-control mb-4'}))
    category_id = forms.ModelChoiceField(label='CATEGORY', queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control mb-4'}))
    content = forms.CharField(label='POST', widget=forms.Textarea(attrs={'class':'form-control mb-4'}))
    

    class Meta:
        model = Post
        fields = ['title','category_id','content']
        widgets = {
            'user_id':widgets.Select(attrs={'class':'form-control'})
        }
        