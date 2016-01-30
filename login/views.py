from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,
from django.http import JsonResponse
from django.core.urlresolvers import reverse

from .forms import RegisterForm, LoginForm, CommentForm

from .models import Users, Comments


def register(request):
    """
    Registers new user via a form field in post
    request and renders the registration form in
    a get request
    """
    data = {}
    if request.method == "POST":
        new_user = RegisterForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            data['success']=1
            data['message'] ="username successfully added"
            return JsonResponse(data)
        else:
            data['success']=0
            data['message']="username registration error"
            return JsonResponse(data)
    else:
        new_user = RegisterForm()
    return render(request, 'login/register.html',
                  {'form':new_user,})

def login(request):
    """
    Checks if a valid username and password in post 
    and renders the login form in get request
    """
    data = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u_obj = Users.objects.filter(username=uname,
                                         password=password)
            if u_obj:
                data['success']=1
                data['message']='login successful'
                return JsonResponse(data)
            else:
                data['success']=0
                data['message']='login error'
                return JsonResponse(data)
    else:
        form = LoginForm()
    return render(request, 'login/login.html',
                      {'form':form,})

def comment(request):
    """
    adds a comment using a post form to db and on get
    renders a comment form
    """
    data = {}
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save()
            data['success']=1
            data['message']='Comment successfully added'
            return JsonResponse(data)
        else:
            data['success']=0
            data['message']='Error while adding comment'
            return JsonResponse(data)
        
    else:
        comment = CommentForm()
    return render(request, 'login/addcomment.html',
                  {'form':comment})

def display(request):
    """
    Returns the entire comments model fields in Json
    """
    data = {}
    comments = Comments.objects.all()
    if comments:
        data['success']=1
        data['message']="Comments available"
        data['comments']=[]
        for i in range(len(comments)):
            data['comments'].append(
                {'username':comments[i].username.username,
                 'comment_id':comments[i].id,
                 'title':comments[i].title,
                 'message':comments[i].message,
                 })
        return JsonResponse(data)
    else:
        data['success']=0
        data['message']='no comments available'
        return JsonResponse(data)
