from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author



# Create your views here.
def index(request):
    num_books = Book.object.all().count()
    num_instances = BookInstance.object.all().count()

    num_instances_available = BookInstance.object.filter(status__exact=2).count
    num_authors = Author.object.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html', context={'num_books': num_books, 'num_instances':num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors':num_authors,
                                                  'num_visits': num_visits})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book
    #template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
