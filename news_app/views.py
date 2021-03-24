from django.shortcuts import render
from .models import News
# Create your views here.


def index(request):
    my_news = News.objects.all()
    return render(request, 'index.html', {'my_news': my_news})

