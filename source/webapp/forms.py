from django import forms
from django.core.validators import EmailValidator
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]




class BookForm(forms.Form):
    name_author = forms.CharField(max_length=100, required=True, label='Имя автора')
    email =forms.EmailField(validators=EmailValidator,label='Почта')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')
    created_at = forms.DateTimeField(auto_now_add=True, label='Время создания')
    updated_at = forms.DateTimeField(auto_now=True, label='Время редактирования')

