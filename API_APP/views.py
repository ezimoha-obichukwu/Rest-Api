from django.shortcuts import render
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
# Create your views here.
def api_home_page(request):
    all_posts = Post.objects.all() #returns a queryset
    new_serialized_data = PostSerializer(all_posts, many=True)
    return Response(new_serialized_data.data)
