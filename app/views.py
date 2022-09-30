from django.shortcuts import render
from .models import Base, Comment
from django.core.paginator import Paginator
from .filters import BaseFilter

import json
import requests

def home(request):
    # fiter based on score(top stories have higher score)
    posts = Base.objects.all().order_by("-score")

    # search filter based on type of story
    type_filter = BaseFilter(request.GET, queryset=posts)
    posts = type_filter.qs

    # paginate
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
        'type_filter': type_filter,
        'page_obj': page_obj,
    }

    return render(request, 'app/home.html', context)

def post(request, pk):
    context = {}
    post = Base.objects.get(post_id=pk)
    comment = Comment.objects.all().filter(parent=pk).order_by("time")

    # check for comment with parent id as post id
    try:
        for i in comment:
            sub_comment = Comment.objects.all().filter(parent=i.comment_id)

        context = {
            'post': post,
            'comment': comment,
            'sub_comment': sub_comment,
        }
        return render(request, 'app/post.html', context)

    except:
        context = {
            'post': post,
            'comment': comment,
        }
    return render(request, 'app/post.html', context)

def new_hn(request):
    posts = Base.objects.all().order_by("-time")
    type_filter = BaseFilter(request.GET, queryset=posts)
    posts = type_filter.qs

    # paginate
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
        'type_filter': type_filter,
        'page_obj': page_obj,
    }

    return render(request, 'app/home.html', context)

def ask_hn(request):
    posts = Base.objects.filter(post_type='Ask HN').order_by("-time")
    type_filter = BaseFilter(request.GET, queryset=posts)
    posts = type_filter.qs

    # paginate
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
        'type_filter': type_filter,
        'page_obj': page_obj,
    }

    return render(request, 'app/home.html', context)

def show_hn(request):
    posts = Base.objects.filter(post_type='Show HN').order_by("-time")
    type_filter = BaseFilter(request.GET, queryset=posts)
    posts = type_filter.qs

    # paginate
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
        'type_filter': type_filter,
        'page_obj': page_obj,
    }

    return render(request, 'app/home.html', context)

def jobs_hn(request):
    posts = Base.objects.filter(post_type='jobs').order_by("-time")
    type_filter = BaseFilter(request.GET, queryset=posts)
    posts = type_filter.qs

    # paginate
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
        'type_filter': type_filter,
        'page_obj': page_obj,
    }

    return render(request, 'app/home.html', context)

def polls_hn(request):
    posts = Base.objects.filter(post_type='polls').order_by("-time")
    type_filter = BaseFilter(request.GET, queryset=posts)
    posts = type_filter.qs

    # paginate
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
        'type_filter': type_filter,
        'page_obj': page_obj,
    }

    return render(request, 'app/home.html', context)
