from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from book.models import Book
# Create your views here.
def index(request):
    books=Book.objects.all()
    return render_to_response("book/index.html",{'books':books})
def detail(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    return render_to_response("book/detail.html",{'book':book})