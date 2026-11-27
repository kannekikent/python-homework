from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POSTS_ON_MAIN = 5


def published_posts():
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
    ).order_by('-pub_date')


def index(request):
    return render(
        request, 'blog/index.html',
        {'post_list': published_posts()[:POSTS_ON_MAIN]},
    )


def post_detail(request, id):
    post = get_object_or_404(published_posts(), pk=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    post_list = published_posts().filter(category=category)
    return render(
        request, 'blog/category.html',
        {'category': category, 'post_list': post_list},
    )
