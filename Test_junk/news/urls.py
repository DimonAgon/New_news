from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('<int:news_id>/', view_news, name='news'),
    path('add', add_post, name='add_news')
]


