from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView

from .forms import BlogPostForm, CommentForm
from .models import BlogPost, Comment


class IntroView(TemplateView):

    template_name = 'blog/intro.html'
    extra_context = {
        'title': 'Welcome'
    }


@login_required
def home(request):
    object_list = BlogPost.objects.all().order_by('-created')
    context = {
        'object_list': object_list,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


@login_required
def detail(request, pk):
    obj = get_object_or_404(BlogPost, pk=pk)
    obj_comments = Comment.objects.filter(post=obj).order_by('-created')
    title = obj.title
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.author = request.user
            instance.post = obj
            instance.save()
            messages.success(request, f"You commented on the post '{obj.title}'.")
            return HttpResponseRedirect(obj.get_absolute_url())
    context = {
        'title': title,
        'object': obj,
        'form': comment_form,
        'comments': obj_comments,
    }
    return render(request, 'blog/detail.html', context)


@login_required
def create(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f"The Post '{title}' was created succesfully!")
            return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'blog/create.html', context)


@login_required
def update(request, pk):
    instance = get_object_or_404(BlogPost, pk=pk)
    if not request.user.username == instance.author.username:
        raise Http404
    form = BlogPostForm(instance=instance)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=instance)
        obj = form.save(commit=False)
        title = obj.title
        obj.save()
        messages.success(request, f"The Post '{title}' was updated successfully! ")
        return HttpResponseRedirect(obj.get_absolute_url())
    context = {
        'form': form,
        'title': 'Update Post'
    }
    return render(request, 'blog/update.html', context)


@login_required
def delete(request, pk):
    obj = get_object_or_404(BlogPost, pk=pk)
    if not request.user.username == obj.author.username:
        raise Http404
    title = obj.title
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f"The Post '{title}' was deleted successfully!")
        return redirect('home')
    context = {
        'object': obj,
        'title': 'Delete Post'
    }
    return render(request, 'blog/delete.html', context)


@login_required
def search(request):
    if request.GET.get('q') is None:
        query = ''
        objects = ''
        print(objects)
    else:
        query = request.GET.get('q')
        objects = BlogPost.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct().order_by('-created')
    context = {
        'title': 'Search',
        'object_list': objects
    }
    return render(request, 'blog/search.html', context)
