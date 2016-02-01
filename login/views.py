from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForm, LoginForm, AboutForm
from .models import Login, About


@csrf_exempt
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

@csrf_exempt
def login(request):
    """
    Checks if a valid username and password in post 
    and renders the login form in get request
    """
    data = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            mob_no = form.cleaned_data.get('mob_no')
            password = form.cleaned_data.get('password')
            u_obj = Login.objects.filter(mobile_number=mob_no,
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
@csrf_exempt
def about(request):
    """
    adds a comment using a post form to db and on get
    renders a comment form
    """
    data = {}
    if request.method == "POST":
        about = AboutForm(request.POST)
        if about.is_valid():
            about.save()
            data['success']=1
            data['message']='Comment successfully added'
            return JsonResponse(data)
        else:
            data['success']=0
            data['message']='Error while adding comment'
            return JsonResponse(data)
        
    else:
        about = AboutForm()
    return render(request, 'login/addcomment.html',
                  {'form':about})
@csrf_exempt
def display(request):
    """
    Returns the entire comments model fields in Json
    """
    data = {}
    about = About.objects.all()
    if about:
        data['success']=1
        data['message']="Comments available"
        data['about']=[]
        for i in range(len(about)):
            data['about'].append(
                {'about':about[i].about,
                 'about_id':about[i].id,
             })
        return JsonResponse(data)
    else:
        data['success']=0
        data['message']='no about available'
        return JsonResponse(data)
