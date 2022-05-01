from .models import Category,Book
def category_links(request):
    category = Category.objects.all()
    return {'categories':category}
