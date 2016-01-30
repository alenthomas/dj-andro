from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .forms import RegisterForm
from .forms import LoginForm

from .models import Users


def register(request):
    if request.method == "POST":
        new_user = RegisterForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return HttpResponseRedirect('/app/success/')
        else:
            return HttpResponseRedirect('/app/error/')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html',
                  {'form':form,})

# login
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u_obj = Users.objects.filter(username=uname, password=password)
            if u_obj:
                return HttpResponseRedirect('/app/successlogin/')
            else:
                return HttpResponseRedirect('/app/errorlogin/')
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
