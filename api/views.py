from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

# Create your views here.

from api.models import Post


@api_view(['GET'])
def getRoutes(req):
    routes = [
        "GET /api/posts/",
        "GET /api/posts/<int:id>",
        "POST /api/posts/",
        "PUT /api/posts/<int:id>",
        "DELETE /api/posts/<int:id>",
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def handle_posts(req):
    if req.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        serializer = PostSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE', 'GET'])
def handle_post(req, pk):
    if req.method == 'GET':
        post = Post.objects.get(uniqueID=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif req.method == 'PUT':
        post = Post.objects.get(uniqueID=pk)
        serializer = PostSerializer(post, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif req.method == 'DELETE':
        post = Post.objects.get(uniqueID=pk)
        post.delete()
        res = {
            'status': 200,
            'message': 'Post with id {} deleted'.format(pk)
        }
        return Response(res)
    return Response(status=400)
