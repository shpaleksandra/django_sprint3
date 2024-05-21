from django.shortcuts import render
from django.http import Http404


def index(request):
    template_name = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    try:
        context = {'post': posts_dict[id]}
    except KeyError:
        raise Http404("Такого поста не существует")
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template_name, context)
