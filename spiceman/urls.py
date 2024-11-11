from django.urls import path
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='spiceman'

urlpatterns = [

    path("login", views.login_and_sighn_up, name="load_login"),
    path("", views.home, name="homepage"),
    path('signup', views.sighnup, name='signup'),
    path("authenticate", views.login_view, name="authenticate"),
    path("create_challenge",views.create_challenge,name="create_challenge"),
    path("add_challenge",views.load_create_challenge,name="create_challenge_page"),
    path("like/<int:challenge_id>",views.like, name ="like"),
    path("challenge_page/<int:challenge_id>",views.challenge_page, name ="challenge_page"),
    path("delete/<int:challenge_id>",views.delete, name="delete"),
    path("weekly_challenges", views.weekly_challenge, name="weekly_challenge"),
    path("search", views.search, name="search"),
    path("logout", views.logoutview, name="logout"),
    path("comments/<int:comment_id>", views.post_comment, name="post_comment"),
    path("comment_like/<int:comment_id>", views.comment_like, name="like_comment"),
    path("delete_comment/<int:comment_id>",views.delete_comment, name="delete_comment"),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)