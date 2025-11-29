from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def posts_by_category(request, category_id):
    # fetch the posts that belongs to category with the id category_id
    posts = Blog.objects.filter(category=category_id, status='Published')
    context = {
        'posts': posts
    }
    return render(request, 'posts_by_category.html', context)