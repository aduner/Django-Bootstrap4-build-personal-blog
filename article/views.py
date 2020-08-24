from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
import markdown


# Create your views here.
def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    # 将markdown语法渲染成html样式
    article.body = md.convert(article.body)

    # 新增了md.toc对象
    context = {'article': article, 'toc': md.toc}
    return render(request, 'article/detail.html', context)
