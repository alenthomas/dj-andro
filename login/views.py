from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .forms import RegisterForm
from .forms import LoginForm

from .models import Users


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
            #return HttpResponseRedirect('/app/success/')
        else:
            data['success']=0
            data['message']="username registration error"
            return JsonResponse(data)
            #return HttpResponseRedirect('/app/error/')
    else:
        new_user = RegisterForm()
    return render(request, 'login/register.html',
                  {'form':new_user,})

# login
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
                #return HttpResponseRedirect('/app/successlogin/')
            else:
                data['success']=0
                data['message']='login error'
                return JsonResponse(data)
                #return HttpResponseRedirect('/app/errorlogin/')
    else:
        form = LoginForm()
    return render(request, 'login/login.html',
                      {'form':form,})
# comments

# add comments

def success(request):
    data = {}
    data['success']=1
    data['message'] ="username successfully added"
    return JsonResponse(data)

def error(request):
    data = {}
    data['success']=0
    data['message']="username registration error"
    return JsonResponse(data)

def login_success(request):
    data = {}
    data['success']=1
    data['message'] ="login successfull"
    return JsonResponse(data)

def login_error(request):
    data = {}
    data['success']=0
    data['message']="login error"
    return JsonResponse(data)


# def status(request, no):
#     no = int(no)
#     data = {}
#     if no == 1:
#         data['success']=1
#         data['message'] ="username successfully added"
#     elif no == 0:
#         data['success']=0
#         data['message'] ="username registration error"
#     else:
#         data = {'error':'unknown'}
#     return JsonResponse(data)
