from django.shortcuts import render, get_object_or_404, redirect
from .models import Article


def index(request):
    articles = Article.objects.order_by('title')
    context = {'articles_list': articles}
    return render(request, 'articles/index.html', context)


def detail(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def like(request):
    assert request.method == 'POST'
    article_id = request.POST['article_id']
    article = get_object_or_404(Article, id=article_id)
    article.likes += 1
    article.save()
    return redirect('articles:detail', article.id)

