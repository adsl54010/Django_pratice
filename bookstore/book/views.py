from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    return render_to_response("book/index.html")
def detail(request,book_id):
    return render_to_response("Book ID=%s" % book_id)