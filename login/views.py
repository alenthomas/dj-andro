from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        new_user = RegisterForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return HttpResponseRedirect(reverse('success'))
            
    else:
        form = RegisterForm()
    return render(request, 'login/register.html',
                  {'form':form,})

# login

# comments

# add comments
