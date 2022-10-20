from django.shortcuts import render
from django.views.generic import DetailView, ListView
from webapp.models import Post


def index(request):
    return render(request, 'webapp/index.html')


def about(request):
    return render(request, 'webapp/about.html')


def menu(request):
    return render(request, 'webapp/menu.html')


def contact(request):
    return render(request, 'webapp/contact.html')


class LBlogView(ListView):
    model = Post
    template_name = 'webapp/blog.html'
    queryset = Post.objects.all().order_by('-created_at')
    context_object_name = 'posts'


class DetailBlogView(DetailView):
    model = Post
    template_name = 'webapp/blog_detail.html'
