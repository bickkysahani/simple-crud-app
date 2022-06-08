from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm

def blogs(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blogs/blogs.html', context)

def blog_detail(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id)
    }
    return render(request, 'blogs/blog_detail.html', context)    


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blogs/'+str(form.instance.id))
        else:
             return HttpResponse('error')
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_create.html', {'form': form})


def blog_update(request,id):
    blog = Blog.objects.get(id=id)
    print(blog.title)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/blogs/'+str(form.instance.id))
        else:
            return HttpResponse('error')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/blog_update.html', {'form': form})


def blog_delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('/')
