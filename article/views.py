from django.shortcuts import render
from django.http import Http404
from article.models import Article
from some_api.models import Book
from django.http import HttpResponse


# Create your views here.
def write_page(request):
    return render(request, 'blog.html')
def per_page(request, id):
    try:
        post = Article.objects.get(id=str(id))
        user_url = request.path
        post_list = Article.objects.all()[:10]
        tag_list = Article.objects.values_list('category', flat=True)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog_list_single.html', {'post':post,'tag_list' : tag_list, 'post_list' : post_list, 'user_url' : user_url})
def home(request):
    post_list = Article.objects.all()
    tag_list = Article.objects.values_list('category', flat=True)
    user_url = request.path
    book_list = Book.objects.all()
    return render(request, 'blog_list.html', {'post_list' : post_list, 'tag_list' : tag_list, 'user_url' : user_url, 'book_list' : book_list})

