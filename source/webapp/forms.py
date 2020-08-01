from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]




class BookForm(forms.Form):
    name_author = forms.CharField(max_length=100, required=True, initial='name',label='Имя автора')
    email =forms.EmailField(label='Почта',initial='email')
    text = forms.CharField(max_length=3000, required=True,initial='text', label='Текст', widget=forms.Textarea)

