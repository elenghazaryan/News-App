from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserForm
from .models import News, Comment, User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_news(request):
    my_news = News.objects.all()
    return render(request, 'all-news.html', {'my_news': my_news})


def detail(request, id):
    news = News.objects.get(pk=id)
    # print(request.user)
    if not request.user.is_authenticated:
        messages.add_message(request, "You're not logged in")
    else:
        if request.method == 'POST':
            # name = request.POST['name']
            # email = request.POST['email']
            comment = request.POST['message']
            Comment.objects.create(
                user_id=id,
                news=news,
                # name=name,
                # email=email,
                comment=comment,
            )
            messages.success(request, "Your comment added successfully")
    comments = Comment.objects.filter(news=news).order_by('-id')
    return render(request, 'detail.html', {'news': news, 'comments': comments})


def register(request):
    form = UserForm
    if request.method == 'POST':
        reg_form = UserForm(request.POST)
        if reg_form.is_valid():
            # User.objects.create(**reg_form)
            reg_form.save()
            messages.success(request, 'User successfully registered.')
    return render(request, 'register.html', {'form': form})

