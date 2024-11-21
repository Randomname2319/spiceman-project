from django.urls import path
from django.urls import path
from . import views

app_name='Y'

urlpatterns = [

    path("login", views.login_and_sighn_up, name="load_login"),
    path("home", views.home, name="homepage"),
    path('signup', views.signup, name='signup'),
    path("authenticate", views.login_view, name="authenticate"),
    path('tweet', views.post_tweet, name='post_tweet'),
    path("hashtag/<str:tag>", views.Hashtag_page, name="Hashtag"),
    path('search', views.search, name='search'),
    path('user/<str:user_name>', views.user_page, name="user_page"),
    path('like/<int:tweet_id>', views.like, name='like'),
    path("delete/int:tweet_author>", views.delete, name="delete")
]
 