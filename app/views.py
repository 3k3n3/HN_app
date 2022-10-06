from django.shortcuts import render
from .models import Base, Comment
from django.core.paginator import Paginator
from .filters import BaseFilter

import json
import requests


from django.utils import timezone
import datetime

def home(request):
##################
# from HN Api
    url = 'https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty'
    payload = "{}"
    response = requests.request("GET", url, data=payload)

    # data is maxitem Id, integer value
    data = response.json()

    pid = []
    counter = 1

    for i in range(data+1):
        i_url = "https://hacker-news.firebaseio.com/v0/item/%d.json" %(data)
        response = requests.get(i_url)
        i_data = response.json()

        time = i_data['time']
        for t in i_data:
            i_data['time'] = datetime.datetime.now(tz=timezone.utc)
    

        if 'dead' in i_data or 'deleted' in i_data:
            pass

        elif i_data['type'] == 'comment':
            pass
            # print(counter,':',i_url[35:],i_data['type'])
            # new_data = Comment(
            #     comment_id = i_data['id'],
            #     by = i_data['by'],
            #     text = i_data['text'],
            #     time = i_data['time'],
            #     comment_type = i_data['type'],
            #     parent=i_data['parent']
            # )
            # new_data.save()
            # if 'kids' in i_data:
            #     for data in i_data['kids']:
            #         i_url = "https://hacker-news.firebaseio.com/v0/item/%d.json" %(data)
            #         print(i_url, 'kid')
            # else: print('NO URL kid')


        elif 'Ask HN' in i_data['title'] or 'Tell HN' in i_data['title']:
            pid.append(i_data['id'])
            new_data = Base(
                post_id = i_data['id'],
                by = i_data['by'],
                score = i_data['score'],
                text = i_data['text'],
                time = i_data['time'],
                title = i_data['title'],
                post_type = 'Ask HN',
            )
            # new_data.save()
            print(counter,':',i_url[35:],'Ask HN')
            counter += 1


            # if 'kids' in i_data:
            #     for data in i_data['kids']:
            #         i_url = "https://hacker-news.firebaseio.com/v0/item/%d.json" %(data)
            #         print(i_url)
            # else: print('Ask HN, no kids')

        elif 'Show HN' in i_data['title']:
            pid.append(i_data['id'])
            
            new_data = Base(
                post_id = i_data['id'],
                by = i_data['by'],
                score = i_data['score'],
                url = i_data['url'],
                time = i_data['time'],
                title = i_data['title'],
                post_type = 'Show HN',
            )
            # new_data.save()
            print(counter,':',i_url[35:],'Show HN')
            counter += 1

            # pid.append(i_data['id'])
            # print(counter,':',i_url[35:],'Show HN')
            # if 'kids' in i_data:
            #     for i in i_data['kids']:
            #         i_url = "https://hacker-news.firebaseio.com/v0/item/%d.json" %(i)
            #         print(i_url)
            #     # print(i_data['kids'])
            # else: print('f them kids')
            # counter += 1

        elif i_data['type'] == 'job':
            pid.append(i_data['id'])

            new_data = Base(
                post_id = i_data['id'],
                by = i_data['by'],
                score = i_data['score'],
                text = i_data['text'],
                time = i_data['time'],
                title = i_data['title'],
                post_type = i_data['type'],
            )
            # new_data.save()
            print(counter,':',i_url[35:],'Job')
            counter += 1

            # print(counter,':',i_url[35:],i_data['type'])
            # if 'kids' in i_data:
            #     for i in i_data['kids']:
            #         i_url = "https://hacker-news.firebaseio.com/v0/item/%d.json" %(i)
            #         print(i_url)
            #     # print(i_data['kids'])
            # else: print('f them kids')
            # counter += 1

        elif i_data['type'] == 'story':
            pid.append(i_data['id'])

            new_data = Base(
                post_id = i_data['id'],
                by = i_data['by'],
                score = i_data['score'],
                url = i_data['url'],
                time = i_data['time'],
                title = i_data['title'],
                post_type = i_data['type'],
            )
            # new_data.save()
            print(counter,':',i_url[35:],'Story')
            counter += 1

            # print(counter,':',i_url[35:],i_data['type'])
            # if 'kids' in i_data:
            #     for i in i_data['kids']:
            #         i_url = "https://hacker-news.firebaseio.com/v0/item/%d.json" %(i)
            #         print(i_url)
            #     # print(i_data['kids'], i_data['descendants'])
            # else: print('f them kids', i_data['descendants'])
            # counter += 1

        else:
            print(counter,':',i_url[35:],i_data['type'], '*UNIQUE*')
            # counter += 1

        data -= 1
        if counter == 11:
            break
    print(pid)
    
########################
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
