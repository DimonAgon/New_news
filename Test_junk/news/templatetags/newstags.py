from django import template

from news.models import Category

register = template.Library()

@register.simple_tag(name='categories_multiplicity')
def get_categories_multiplicity():
    return Category.objects.all()

# @register.inclusion_tag('tags/news_blocks')
# def show_news():


