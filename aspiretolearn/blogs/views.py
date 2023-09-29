from django.shortcuts import render
from .models import Post, Category, Comments
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm,CommentForm,LogInForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blogs:home')
    else:
        form = LogInForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def home(request):
    post_obj = Post.objects.all()
    post_last = Post.objects.all()[:3]
    category_obj = Category.objects.all()
    return render(request,'blogs/home.html',{'post':post_obj,
                                             'category':category_obj,
                                             'post_last':post_last})

@login_required
def single_blog(request,post_id=None):
    if request.method == 'POST':
        Comments.objects.create(post_id=request.POST.get('post_id'),
                                author_id=request.user.id,
                                comment=request.POST.get('comment'))
    try:
        po_obj = Post.objects.get(id=post_id)
    except:
        po_obj = None
    post_last = Post.objects.all()[:4]
    form = CommentForm()
    comm = Comments.objects.filter(post_id=post_id)
    cat = Category.objects.all()
    all_list = []
    for i in cat:
        small_list = []
        small_list.append(i.id)
        small_list.append(i.category)
        small_list.append(len(list(Post.objects.filter(category_id=i.id))))
        all_list.append(small_list)
    return render(request,'blogs/single.html',{'po_obj':po_obj,
                                               'post_last':post_last,
                                               'form':form,
                                               'post_id':post_id,
                                               'comm':comm,
                                              'category_obj':all_list,})
@login_required
def category(request,cat_id=None):
    try:
        cat_obj = Category.objects.get(id=cat_id)
    except:
        cat_obj = None
    try:
        po_obj = Post.objects.filter(category_id=cat_id)
    except:
        po_obj = None
    all_list = []
    cat = Category.objects.all()
    for i in cat:
        small_list = []
        small_list.append(i.id)
        small_list.append(i.category)
        small_list.append(len(list(Post.objects.filter(category_id=i.id))))
        all_list.append(small_list)
    return render(request,'blogs/category.html',{'cat_obj':cat_obj,
                                                 'po_obj':po_obj,
                                                 'category_obj':all_list,})

@login_required
def about(request):
    return render(request,'blogs/about.html')

@login_required
def contact(request):
    return render(request,'blogs/contact.html')

@login_required
def search_result(request):
    print(request.GET.get('content'))
    try:
        matching_posts = Post.objects.filter(title__icontains=request.GET.get('content'))
    except:
        matching_posts = None
    print(matching_posts,'matching_posts')
    return render(request,'blogs/search-result.html', {'data': matching_posts,
                                                       'searched_item':request.GET.get('content')})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if not (User.objects.filter(username=request.POST.get('username')) or User.objects.filter(email=request.POST.get('email'))):
                user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
                user.email = request.POST.get('email')
                user.save()
                return redirect('blogs:home')
        return render(request, 'account/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})