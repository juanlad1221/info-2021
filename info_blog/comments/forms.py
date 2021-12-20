from django import forms
from django.forms import fields, widgets
from django.utils.translation import gettext_lazy as _
from .models import Comments

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

        