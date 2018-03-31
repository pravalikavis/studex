from django.shortcuts import render

from django.utils import timezone
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,UserRegistrationForm,CommentForm
from django import forms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg



# Create your views here.
def cards(request):
    query = request.GET.get("q")

    if query:

        post = Post.objects.filter(title__icontains=query)
    else:
        post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/cards.html', {'post': post, })


def homepage(request):
    post = Post.objects
    post=post.order_by('comments')

    return render(request, 'blog/homepage.html', {'post':post, })


def post_sort(request,q):
    post=Post.objects
    comment=Comment.objects
    if q=='1':
        post=post.order_by('title')

    if q=='2':
        post=post.order_by('title').reverse()
    if q=='3':
        post=post.filter(published_date__lte=timezone.now()).order_by('published_date')
    if q=='4':
        post=post.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()


    return render(request, 'blog/cards.html', {'post': post})

def post_detail(request, pk):
    query = request.GET.get("q")

    if query:

        post = Post.objects.filter(title__icontains=query)
        return render(request, 'blog/cards.html', {'post': post, })
    else:
        post = get_object_or_404(Post, pk=pk)
        comment = Comment.objects.filter(post=post).aggregate(Avg('rating'))
        return render(request, 'blog/post_detail.html', {'post': post,'comment':comment,})

def add_comment_to_post(request, pk):
    query = request.GET.get("q")

    if query:
        post = Post.objects.filter(title__icontains=query)
        return render(request, 'blog/post_list.html', {'post': post, })
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def signup(request):
    return render(request, 'blog/signup.html', {})

def upload(request):
    return render(request, 'blog/upload.html', {})


def aboutus(request):
    return render(request, 'blog/aboutus.html', {})
def register(request):
    query = request.GET.get("q")

    if query:
        post = Post.objects.filter(title__icontains=query)
        return render(request, 'blog/cards.html', {'post': post, })
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists()):
                '''or User.objects.filter(email=email).exists())'''
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/signup.html', {'form' : form})

def logout_view(request):

    logout(request)
    return render(request,'register/logged_out.html')