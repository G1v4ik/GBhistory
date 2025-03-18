from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blogs.models import Category


def index(request):

    categories = Category.objects.all()

    return render(request, 'html/index.html',{
        "categories":categories,
    })

