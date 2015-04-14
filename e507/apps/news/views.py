from django.shortcuts import render, get_object_or_404

import e507.apps.news.models
import e507.apps.news.forms


def home_view(request):
    latest_news_list = e507.apps.news.models.News.objects.order_by('-start_date')[:5]
    return render(request, 'news/home.html', {
        'latest_news_list': latest_news_list
    })


def detail_view(request, news_id):
    news = get_object_or_404(e507.apps.news.models.News, pk=news_id)
    return render(request, 'news/detail.html', {
        'news': news
    })


def add_view(request):
    added = False
    invalid_form = False

    if request.method == 'POST':
        form = e507.apps.news.forms.NewsForm(request.POST)
        if form.is_valid():
            news_title = form.cleaned_data['title']
            news_message = form.cleaned_data['message']
            news = e507.apps.news.models.News(title=news_title, message=news_message)
            news.save()
            added = True
        else :
            invalid_form = form.errors
    else :
        form = e507.apps.news.forms.NewsForm()

    return render(request, 'news/add.html', {
        'form' : form,

        'added_alert' : added,
        'invalid_form_alert' : invalid_form,
    })
