from django.contrib import admin
from .models import Category, News

# Register your models here.
admin.site.register(Category)


class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')


admin.site.register(News, AdminNews)

