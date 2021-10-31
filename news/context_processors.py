from news.models import Category


def add_variable_to_context(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }
