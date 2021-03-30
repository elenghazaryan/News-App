from django.contrib import admin
from .models import Category, News, Comment

# Register your models here.
admin.site.register(Category)


class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')


class AdminComments(admin.ModelAdmin):
    list_display = ('news', 'email', 'comment')


admin.site.register(News, AdminNews)
admin.site.register(Comment, AdminComments)
