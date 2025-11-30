from .models import Category

# whatever it's returning is available in all templates
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)