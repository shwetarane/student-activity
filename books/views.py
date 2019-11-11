from django.shortcuts import render, get_object_or_404
from .models import Book
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import BookSearchForm
from django.http.response import Http404

# Create your views here.
@login_required
def book_list(request):

    books = Book.objects.all()
    paginator = Paginator(books,3)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'books/list.html',\
        {
            'books':books,
        })

@login_required
def book_detail(request, slug=None):
    book = get_object_or_404(Book,slug=slug)
    return render(request,'books/book_detail.html',
                {'book':book,
                })
@login_required
def book_search(request):

    form = BookSearchForm()
    a_name = b_name = isbn = None
    results = []   
    if 'book_name' in request.GET:
        form = BookSearchForm(request.GET)
        form.full_clean()

        a_name = form.cleaned_data['author_name']
        b_name = form.cleaned_data['book_name']
        isbn = form.cleaned_data['isbn']
        if a_name!='' and b_name!='' and isbn !='':
            results = Book.bmanager_obj.get_by_all_values(a_name=a_name,
                                                        b_name=b_name,
                                                        isbn=isbn)
        else:
            if a_name !='' and b_name!= '':
                results = Book.bmanager_obj.get_by_b_name_and_a_name(b_name=b_name,\
                                                                    a_name=a_name)
            elif a_name !='' and isbn!= '':
                results = Book.bmanager_obj.get_by_a_name_and_isbn(a_name=a_name,
                                                                        isbn=isbn)
            elif b_name !='' and isbn != '':
                results = Book.bmanager_obj.get_by_b_name_and_isbn(b_name=b_name,\
                                                                        isbn=isbn)
            elif a_name !='' and b_name =='' and isbn =='':
                results = Book.bmanager_obj.get_by_author_name(a_name=a_name)
            elif b_name !='' and a_name == '' and isbn =='':
                results = Book.bmanager_obj.get_by_book_name(b_name=b_name)
            elif isbn !='' and a_name =='' and b_name =='':
                results = Book.bmanager_obj.get_by_isbn(isbn=isbn)

        if results.count() == 0:
            raise Http404("No match is availabe for the given query -- author-name == %s ; \
                published-name ==%s;  Book-name == %s " \
                    %(a_name,isbn,b_name))
    return render(request,'books/book_search.html',{'form':form,\
            'results':results})