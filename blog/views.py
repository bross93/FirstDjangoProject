from django.shortcuts import render
# Remeber to fucking import you doofus
from .models import Post
from .models import Practice
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def home_view(request):
	return render(request, 'blog/home.html')

def news_page(request):
	return render(request, 'blog/news.html')

def overview_page(request):
	return render(request, 'blog/overview.html')

def about_page(request):
	return render(request, 'blog/about.html')

def practitioner_blog(request):
	return render(request, 'blog/therapist_blogs.html')

def practice_list(request):
	practices = Practice.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog/practice_list.html', {'practices': practices})

def practice_detail(request, pk):
	practice = get_object_or_404(Practice, pk=pk)
	return render(request, 'blog/practice_detail.html', {'practice': practice})

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})