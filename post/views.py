from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
	return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(req, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(req, 'post/post_detail.html', {'post': post})

def post_new(req):
	if req.method == "POST":
		form = PostForm(req.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = req.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()

	return render(req, 'post/post_edit.html', {'form': form})

def post_edit(req, pk):
	post = get_object_or_404(Post, pk=pk)
	if req.method == "POST":
		form = PostForm(req.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = req.user
			post.published_at = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(req, 'post/post_edit.html', {'form': form})

def post_draft_list(req):
	posts = Post.objects.filter(published_at__isnull=True).order_by('created_at')
	return render(req, 'post/post_draft_list.html', {'posts': posts})