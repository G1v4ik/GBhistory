from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogCollect, BlogContent


def getMainPage(request):

    getBlogCollect = BlogCollect.objects.all()

    return render(request,'html/main.html', {
        "datablog":{
            "blogcollect":getBlogCollect,
        }
    })

def getBlogDetail(request, slug):
    blogCollect_name = get_object_or_404(BlogCollect, slug=slug)
    blogList = Blog.objects.filter(blogcollect=blogCollect_name)

    

    return render(request, 'html/BlogListOneThems.html', {"b":{
        "blog":blogList
    }})

