from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogPostForm, CategoryForm
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

from django.template.defaultfilters import slugify

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
   
    return render(request, 'dashboard/dashboard.html', {
        "category_count": category_count, 
        "blogs_count" : blogs_count
    })

def categories(request):
    print(request.path)
    return render(request, "dashboard/categories.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request,"dashboard/add_category.html", context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context =  {
        'form': form, 
        'category':category
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
     category = get_object_or_404(Category, pk=pk)
     category.delete()
     return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request,"dashboard/posts.html", context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            # set temporary slug based on title
            title = form.cleaned_data['title']
            post.slug = slugify(title)  # temporary
            
            post.save()  # saves once, now post.id exists
            
            # update slug with id to ensure uniqueness
            post.slug = f"{slugify(title)}-{post.id}"
            post.save()

            return redirect('posts')

        else:
            print("Invalid")
            print(form.errors)

    form = BlogPostForm()
    return render(request, 'dashboard/add_post.html', {"form": form})

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = f"{slugify(title)}-{post.id}"
            post.save()
            return redirect('posts')

    form = BlogPostForm(instance=post)
    context = {
        "form": form,
        'post': post
    }
    return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')


