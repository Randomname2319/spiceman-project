from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tweet
from .models import Hashtag
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login_and_sighn_up(request):
    return render(request, 'y/sighn_up_login.html')

def home(request):
    return render(request, 'y/homepage.html', context={'tweets':Tweet.objects.order_by('-post_date')})

def signup(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)

    user = User.objects.create_user(username=username, password=password)

    if user:
        login(request, user) 

        return redirect('Y:homepage')
    
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
        return redirect('Y:homepage')
    else:
        return redirect('Y:load_login')

def post_tweet(request):
    tweet = request.POST['tweet_text']
    print(tweet)
    t = Tweet(post_text=tweet, author=request.user)
    t.save() 

    words = tweet.split()
    for word in words:
        if word[0] == "#":
            process_hashtag(word, t)

    return redirect('Y:homepage')

def process_hashtag(tag, tweet):

    try:
        hash = Hashtag.objects.get(hashtag_text=tag)
    except Hashtag.DoesNotExist:
        hash = Hashtag(hashtag_text=tag)
        hash.save()
    
    hash.tweets.add(tweet)


def search(request):
    tag = request.GET['hash']
    if not tag.startswith('#'):
        tag = '#' + tag

    return redirect('Y:Hashtag', tag=tag)


def Hashtag_page(request, tag):
    h = Hashtag.objects.get(hashtag_text=tag)
    return render(request, 'y/Hashtag_page.html', {'hash': h, 'tweets': h.tweets.all() })
    
        
def user_page(request, user_name):
    user = User.objects.get(username=user_name)
    tweets = user.author.all()
    return render(request, "y/user_page.html", {'author':user, 'tweets': tweets})
     
def like(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if request.user in tweet.likers.all() :
        tweet.likers.remove(request.user)
    else:
        tweet.likers.add(request.user)
    
    return redirect(request.META['HTTP_REFERER'])

def delete(request):
    tweet = Tweet.objects.get()
    tweet.delete()
    return redirect(request.META['HTTP_REFERER'])

