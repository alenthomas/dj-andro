from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .forms import RegisterForm
# Create your views here.
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
