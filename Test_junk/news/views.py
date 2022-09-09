from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category

from .forms import NewsForm


def index(request):
    news_multiplicity = News.objects.all()
    context = {
        'news_var': news_multiplicity,
        'title': 'НОВЫЕ НОВОСТИ'}
    return render(request, r'news\index.html', context=context)


def get_category(request, category_id):
    news_multiplicity = News.objects.filter(category_id=category_id)
    curr_category = Category.objects.get(pk=category_id)
    context = {'news_var': news_multiplicity,
               'title': curr_category.title,}
    return render(request, r'news\category.html', context=context, )


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {'n': news_item}
    return render(request, r'news/check_news.html', context=context)

def add_post(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new_news = News.objects.create(**form.cleaned_data)
            return redirect(new_news)
    else:
        form = NewsForm()

    return render(request, r'news/add_news.html', {'form': form})




