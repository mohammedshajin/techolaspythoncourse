from django.shortcuts import render, redirect

from . models import Post
from . forms import PostForm

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def blog(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'blog.html', context)

def createpost(request):
    user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.user = user
            post.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'createpost.html', context)


def updatepost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post= form.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'createpost.html', context)

def deletepost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')
