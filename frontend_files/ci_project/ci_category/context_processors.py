from ci_category.models import Category

# menu links will be available in all templates
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
