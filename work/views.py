from django.shortcuts import render, get_object_or_404, reverse
from . models import Post
from django.views import generic, View


# Create your views here.
class Post(generic.ListView):
    model = Post
    template_name = 'work/post.html'
    context_object_name = 'posts'
    ordering = ['-created_on']
    paginate_by = 3

