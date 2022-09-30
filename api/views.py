from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BaseSerializer
from app.models import Base


@api_view(['GET'])
def overview(request):
    # urls for api
    urls = {
        'Overview' : 'http://127.0.0.1:8000/api',
        'All Posts' : 'http://127.0.0.1:8000/api/get',
        'Get Post' : 'http://127.0.0.1:8000/api/get/<pk>',
        'Add Post' : 'http://127.0.0.1:8000/api/post',
        'Delete Post' : 'http://127.0.0.1:8000/api/delete/<pk>',
        'pk' : 'Post ID',
    }

    return Response(urls)


@api_view(['GET'])
def all_posts(request):
    posts = Base.objects.all()
    serializer = BaseSerializer(posts, many=True) #serializing multiple items

    return Response(serializer.data)

@api_view(['GET'])
def get_post(request,pk):
    try:
        post = Base.objects.get(post_id=pk)
        serializer = BaseSerializer(post)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_post(request):
    serializer = BaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = Base.objects.get(post_id=pk)
        if pk:
            post.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
