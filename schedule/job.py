from app.models import Base, Comment
from django.utils import timezone
import requests
import json
import datetime


def schedule_job():
    # from HN Api
    url = 'https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty'
    payload = "{}"
    response = requests.request("GET", url, data=payload)

    # data is maxitem Id, integer value
    data = response.json()

    global pid, counter, i_data
    pid = []
    counter = 1


    for i in range(data+1):
        i_url = "https://hacker-news.firebaseio.com/v0/item/%d.json" %(data)
        response = requests.get(i_url)
        i_data = response.json()

        # For time object in new_data format from unix time to regular time
        time = i_data['time']
        for t in i_data:
            i_data['time'] = datetime.datetime.now(tz=timezone.utc)

        #check if item is dead/deleted and pass
        if 'dead' in i_data or 'deleted' in i_data:
            pass
        
        # send comments to comments model
        elif i_data['type'] == 'comment': 
            pass
            # new_data = Comment(
            #     comment_id = i_data['id'],
            #     by = i_data['by'],
            #     text = i_data['text'],
            #     time = i_data['time'],
            #     comment_type = i_data['type'],
            #     parent=i_data['parent']
            # )
            # new_data.save()
        
            '''
            Check if story type is Ask HN or Show HN first because they have some 
            unique fields from regular HN stories, then save them as their own type.
            Increment counter by one at each instance an item is saved to Base model.
            '''
        elif 'Ask HN' in i_data['title'] or 'Tell HN' in i_data['title']:
            update_db()
            # print(counter,':',i_url[35:],'Ask HN')
            counter += 1

        elif 'Show HN' in i_data['title']:
            update_db()
            # print(counter,':',i_url[35:],'Show HN')
            counter += 1

        elif i_data['type'] == 'job':
            update_db()
            # print(counter,':',i_url[35:],'Job')
            counter += 1

        elif i_data['type'] == 'story':
            update_db()
            # print(counter,':',i_url[35:],'Story')
            counter += 1


        # if for there is a post type not recognized output to terminal
        else: print(f'Post type {i_data["type"]} not recognized at {counter}')

        # decrease maxitem id by one on each iteration
        data -= 1
        if counter == 11:
            break

# functions to save data to db
def update_db():
    pid.append(i_data['id'])
    if 'url' in i_data:
        has_url()
    elif 'text' in i_data:
        has_text()
    else:
        no_text_url()

def has_url():
    new_data = Base(
        post_id = i_data['id'],
        by = i_data['by'],
        score = i_data['score'],
        url = i_data['url'],
        time = i_data['time'],
        title = i_data['title'],
        post_type = i_data['type'],
        # post_type = 'Show HN', # to specify cetain story types for example, 
    )
    new_data.save()

def has_text():
    new_data = Base(
        post_id = i_data['id'],
        by = i_data['by'],
        score = i_data['score'],
        text = i_data['text'],
        time = i_data['time'],
        title = i_data['title'],
        post_type = i_data['type'],
    )
    new_data.save()

def no_text_url():
    new_data = Base(
        post_id = i_data['id'],
        by = i_data['by'],
        score = i_data['score'],
        time = i_data['time'],
        title = i_data['title'],
        post_type = i_data['type'],
    )
    new_data.save()
