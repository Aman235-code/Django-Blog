from django.shortcuts import render

from assignments.models import About
from blogs.models import Category, Blog

def home(request):
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    try: 
        about = About.objects.get()
    except:
        about = None
    return render(request, 'home.html', {'featured_posts': featured_posts, 'posts': posts, 'about': about})