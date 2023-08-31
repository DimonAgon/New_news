from django.forms import ModelForm, TextInput, Textarea, Select, ImageField
from django.core.exceptions import ValidationError
from .models import News
from os.path import getsize
import re


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'category', 'photo')
        widgets = {
            'title': TextInput(
                attrs={'id': 'stretchable_input', 'class': 'news-form title-form mt-2', 'autofocus': True,
                       'required': True}),
            'content': Textarea(
                attrs={'id': 'stretchable_area', 'class': 'news-form content-form stretchable', 'rows': 4,
                       'data-min-rows': 4, 'required': True}),
            'category': Select(attrs={'class': 'news-form category-form'}),
        }
        labels = {
            'title': "Событие, заголовок",
            'content': "Содержание",
            'category': "Категория: ",
            'photo': "Фото"
        }

        error_messages = {
            'name': "Слишком длинное название"
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if re.match('\d', title):
                raise ValidationError('Название не должно начинаться с цифры')
            return title

        def clean_photo(self):
            photo = self.cleaned_data['photo']
            if getsize(photo) > 99 * 1024:  # counting in mbytes
                raise ValidationError('Слишком большой файл')
            return photo
