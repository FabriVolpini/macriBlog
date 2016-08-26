from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def posts_list(request):
    posts = Post.objects.filter(fechita__lte=timezone.now()).order_by('fechita')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_zoom(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_zoom.html', {'post': post})

def calculadora(request):
    return render(request, 'posts/calculadora.html')

def cronometro(request):
    return render(request, 'posts/cronometro.html')

def conversor(request):
    return render(request, 'posts/conversor.html')

def chboton(request):
    return render(request, 'posts/chboton.html')