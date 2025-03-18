from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User

from .models import Post, Category
from .forms import AddPostForm

def post_of_theme(request, slug_theme):

    posts = Post.objects.filter(category=Category.objects.get(slug=slug_theme))

    return render(request, 'html/post_of_theme.html', {
        'posts':posts
    })


def post_detail(request, slug_theme, slug_post):
    
    post = Post.objects.get(slug=slug_post)

    return render(request, 'html/post_detail.html', {
        'post':post,
    })


def post_my(request, user_id):

    posts = Post.objects.filter(author=User.objects.get(id=user_id))

    return render(request, 'html/post_my.html', {
        "posts": posts
    })


class AddPostView(CreateView):
    form_class = AddPostForm
    template_name = 'html/post_add.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        return super().form_valid(form)