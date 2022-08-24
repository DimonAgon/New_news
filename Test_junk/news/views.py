from django.shortcuts import render

from .models import News, Category


def index(request):
    news_multiplicity = News.objects.all()
    context = {
        'news_var': news_multiplicity,
        'title': 'НОВЫЕ НОВОСТИ'}
    return render(request, 'news\index.html', context=context)


def get_category(request, category_id):
    news_multiplicity = News.objects.filter(category_id=category_id)
    curr_category = Category.objects.get(pk=category_id)
    context = {'news_var': news_multiplicity,
               'title': curr_category.title}
    return render(request, r'news\category.html', context=context)


def view_news(request, news_id):
     news_item = News.objects.get(pk=news_id)
     return render(request, '')
