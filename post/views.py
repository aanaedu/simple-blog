from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
	return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(req, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(req, 'post/post_detail.html', {'post': post})