from django import forms
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from .models import Comments
from post.models import Category, Post

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment', 'email','post_id']
        widgets ={
            'comment':widgets.Textarea(attrs={'class':'form-control', 'width':'40px'}),
            'email':widgets.EmailInput(attrs={'class':'form-control', 'requerid':True}),
            'post_id':widgets.HiddenInput()
        }
        labels = {
            'comment': _('Comentarios'),
        }


class newCommentForm(forms.ModelForm):
    comment = forms.CharField(label='COMMENT', widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.EmailField(label='EMAIL', widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Comments
        fields = ['comment','email','post_id']
        widgets={
            'post_id':widgets.Select(attrs={'class':'form-control'})
        }
        labels = {
            'post_id': _('POST'),
        }


class editCommentForm(forms.ModelForm):
    comment = forms.CharField(label='COMMENT', widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.EmailField(label='EMAIL', widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = Comments
        fields = ['comment','email']
        
