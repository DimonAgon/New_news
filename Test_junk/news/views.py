from django.shortcuts import render, get_object_or_404
from .models import News, Category


def index(request):
    news_multiplicity = News.objects.all()
    context = {
        'news_var': news_multiplicity,
        'title': 'НОВЫЕ НОВОСТИ',
        'parameter': 'home_page'}
    return render(request, 'news\index.html', context=context)


def get_category(request, category_id):
    news_multiplicity = News.objects.filter(category_id=category_id)
    curr_category = Category.objects.get(pk=category_id)
    context = {'news_var': news_multiplicity,
               'title': curr_category.title,
               'parameter': 'category_page'}
    return render(request, r'news\category.html', context=context, )


def view_news(request, news_id):
        news_item = get_object_or_404(News, pk=news_id)
        context = {'news_var': [news_item],
                    'parameter': 'news_page'}
        return render(request, r'news/view_news_temp.html', context=context)

