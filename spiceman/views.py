from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Challenge, Comment


def login_and_sighn_up(request):
    return render(request, 'spiceman/login_sighnup.html')


def home(request, challenges=None, search=True):
    if not challenges:
        challenges = Challenge.objects.all()

    return render(request, 'spiceman/homepage.html', {'challenges':challenges, 'search_results':search})


def sighnup(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)

    user = User.objects.create_user(username=username, password=password)

    if user:
        login(request, user) 

        return redirect('spiceman:homepage')
    
    return HttpResponse('did not work')


def login_view(request):
    print('in Login View')
    username = request.POST["username"]
    password = request.POST["password"]
    print(username, password)
    user = authenticate(request, username=username, password=password)
    print(user)

    if user is not None:
        print(f'User {username} authenticated. Logging in now...')
        login(request, user)    
        return redirect('spiceman:homepage')
    else:
        return redirect('spiceman:load_login')

def load_create_challenge(request):
    return render(request, 'spiceman/create_challenge.html')

def create_challenge(request):
    print(request.POST)
    challenge = request.POST["text"]
    name = request.POST["title"]
    chilli = request.POST["chilli_number"]
    answer = request.POST["challenge_answer_text"]
    weekly = request.POST.get("weekly_challenges", '')
    try:
        answer_image = request.FILES["challenge_answer_image"]
        c = Challenge(text=challenge, author=request.user, title=name,  difficulty=chilli, answer_text=answer, answer_image=answer_image)
    except:
        c = Challenge(text=challenge, author=request.user, title=name,  difficulty=chilli, answer_text=answer)
    print(challenge)

    
    c.save()

    print(weekly)
    print(type(weekly))

    if weekly == 'on':
        c.isweekly = True
        c.save()

    return redirect("spiceman:homepage")


def like(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    if request.user in challenge.likers.all() :
        challenge.likers.remove(request.user)
    else:
        challenge.likers.add(request.user)
    
    return redirect(request.META['HTTP_REFERER'])


def comment_like(request, comment_id):
    
    comment = Comment.objects.get(id=comment_id)
    if request.user in comment.likers.all() :
        comment.likers.remove(request.user)
    else:
        comment.likers.add(request.user)
    
    return redirect(request.META['HTTP_REFERER'])

def delete_comment(request, comment_id):
    print(f'Deleting comment: {comment_id}')
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(request.META['HTTP_REFERER'])




def delete(request, challenge_id):
    print(f'Deleting challenge: {challenge_id}')
    challenge = Challenge.objects.get(id=challenge_id)
    challenge.delete()
    return redirect(request.META['HTTP_REFERER'])


def challenge_page(request,challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    return render(request, 'spiceman/challenge.html', {'challenge':challenge})

def weekly_challenge(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    if challenge.isweekly == True:
        return render(request, 'spiceman/weekly_challenges.html')
    

def search(request):
    search_term = request.GET["search_bar"]
    if not search_term:
        return home(request, search=False)
    
    challenges = Challenge.objects.filter(title__icontains=search_term).union(Challenge.objects.filter(text__icontains=search_term))
    if len(challenges) > 0:
        return home(request, challenges, search=True)
    else:
        return home(request, challenges, search=False)

def post_comment(request, comment_id):
    text = request.POST['text']
    com = Comment(text=text, author=request.user, challenge=Comment.objects.get(id=comment_id))

    com.save() 
    
    return redirect(request.META['HTTP_REFERER'])

def logoutview(request):
    logout(request)
    return redirect ('spiceman:load_login')


