from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]




class BookForm(forms.Form):
    name_author = forms.CharField(max_length=100, required=True, initial='Name',label='Имя автора')
    email =forms.EmailField(label='Почта',initial='EmailAdress')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=forms.Textarea)

