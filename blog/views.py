from django.shortcuts import render, get_object_or_404
from .models import blogs


def all_blogs(request):
    blog = blogs.objects.order_by('-date')
    return render(request, 'blog/all_blog.html', {'blog': blog})


def detail(request, blog_id):
    blog = get_object_or_404(blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
