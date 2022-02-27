from django.contrib import admin
from .models import Article, Tag, ArticleScope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main'):
                is_main_count += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if is_main_count == 0:
            raise ValidationError('Выберите основной тег')
        if is_main_count > 1:
            raise ValidationError('Основной тег может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 6
    formset = ArticleScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass