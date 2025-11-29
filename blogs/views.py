from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):

    # fetch the posts that belongs to category with the id category_id
    posts = Blog.objects.filter(category=category_id, status='Published')

    # use this when you want to redirect to home page if category not found
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     # redirect to home page 
    #     return redirect('home')
    
    # Use this when you want to show 404 error page if category not found
    category = get_object_or_404(Category, id=category_id)

    context = {
        'posts': posts,
        'category': category
    }

    return render(request, 'posts_by_category.html', context)