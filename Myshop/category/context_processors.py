from .models import Category

def menu_links(request):
    data = Category.objects.all()
    return dict(links=data)