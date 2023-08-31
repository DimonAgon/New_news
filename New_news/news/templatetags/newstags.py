from django import template

from news.models import Category

register = template.Library()


@register.simple_tag(name='categories_multiplicity')
def get_categories_multiplicity():
    return Category.objects.all()


#@register.inclusion_tag()
# def show_news_blocks():
#     pass


# TODO: Plan for fourth-level inheritance
# Inside the second-level template, call a tag that calls a third-level template, with an argument pointing to the fourth-level template
