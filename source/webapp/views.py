from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, Http404
from webapp.models import Book,STATUS_CHOICES
from webapp.forms import BookForm




def index_view(request):

    book = Book.objects.all()
    context = {
        'book': book
    }
    return render(request, 'index.html', context)


def book_view(request, pk):

    book = get_object_or_404(Book, pk=pk)

    context = {'book': book}
    return render(request, 'book_view.html', context)

# def index_view(request):
#     is_admin = request.GET.get('is_admin', None)
#     if is_admin:
#         data = Book.objects.all()
#     else:
#         data = Book.objects.filter(status='active')
#     return render(request, 'index.html', context={
#         'book': data
#     })




# def book_create(request):
#     if request.method == "GET":
#         return render(request, 'book_create.html', context={
#             'status_choices': STATUS_CHOICES
#         })
#     elif request.method == 'POST':
#         name_author = request.POST.get('name_author')
#         email = request.POST.get('email')
#         text = request.POST.get('text')
#         status = request.POST.get('status')
#         book = Book.objects.create(name_author=name_author, email=email,text=text,status=status)
#         context = {'book': book}
#         return render(request, 'book_view.html', context)


def book_create(request):
    if request.method == "GET":
        return render(request, 'book_create.html', context={
            'form': BookForm()
         })
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(
                name_author=form.cleaned_data['name_author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'book_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])



def book_update_view(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "GET":
        form = BookForm(initial={
            'name_author': book.name_author,
            'email': book.email,
            'text': book.text,
        })
        return render(request, 'book_update.html', context={
            'form': form,
            'book': book
        })
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.name_author = form.cleaned_data['name_author']
            book.email = form.cleaned_data['email']
            book.text = form.cleaned_data['text']
            book.save()
            return redirect('index',pk=book.pk)
        else:
            return render(request, 'book_update.html', context={
                'book': book,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])



def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
       return render(request, 'book_delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('index')
