from django.shortcuts import render

from webapp.models import Book,STATUS_CHOICES


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Book.objects.all()
    else:
        data = Book.objects.filter(status='moderated')
    return render(request, 'index.html', context={
        'articles': data
    })



def book_create(request):
    if request.method == "GET":
        return render(request, 'book_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        name_author = request.POST.get('name_author')
        email = request.POST.get('email')
        text = request.POST.get('text')
        status = request.POST.get('status')
        book = Book.objects.create(name_author=name_author, email=email,text=text,status=status)
        context = {'article': book}
        return render(request, 'book_view.html', context)
