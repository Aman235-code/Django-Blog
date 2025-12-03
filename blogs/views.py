from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Category, Comment
from django.db.models import Q # for complex queries like OR operations

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

def blogs(request, blog_slug):
    single_blog = get_object_or_404(Blog, slug=blog_slug, status='Published')
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=single_blog)
    oomments_count = comments.count()
    return render(request, 'blogs.html', {'single_blog': single_blog, "comments": comments,"oomments_count":oomments_count})

def blog_search(request):
    keyword = request.GET.get('keyword') 
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published' )
    return render(request, 'blog_search.html', {'blogs': blogs, 'keyword': keyword})