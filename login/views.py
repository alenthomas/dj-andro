from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForm, LoginForm, AboutForm
from .models import Login, About, Team, Score


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

def score(request):
    """
    Return the team names and scores
    """
    # if request.method == POST:
    #     form = ScoreForm(request.POST)
    #     if form.is_valid():
    #         team1=form.cleaned_data.get('team1')
    #         team2=form.cleaned_data.get('team2')
    team1 = Team.objects.filter(team_id='team1')
    team2 = Team.objects.filter(team_id='team2')
    score1 = Score.objects.filter(team__team_id='team1')
    score2 = Score.objects.filter(team__team_id='team2')
    return render(request, 'login/score.html',{
        't1':team1[0],
        't2':team2[0],
        's1':score1[0],
        's2':score2[0],
        })

def scorejson(request):
    """
    Return the team names and scores
    """
    team1 = Team.objects.filter(team_id='team1')
    team2 = Team.objects.filter(team_id='team2')
    score1 = Score.objects.filter(team__team_id='team1')
    score2 = Score.objects.filter(team__team_id='team2')
    data = {}
    score = Score.objects.all()
    if score:
        data['success']=1
        data['message']="Current Score Available"
        data['score'] = []
        for i in range(len(score)):
            data['score'].append(
                {'score':score[i].score,
                 'team_name':score[i].team.team,
                 'team_id':score[i].team.team_id,
                 })
        return JsonResponse(data)
    else:
        data['success']=0
        data['message']='no score available'
        return JsonResponse(data)
    # return render(request, 'login/score.html',{
    #     't1':team1[0],
    #     't2':team2[0],
    #     's1':score1[0],
    #     's2':score2[0],
    #     })
