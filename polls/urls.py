from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "polls"

urlpatterns  = [
    path("home", views.index, name='hompage'),
    path("questions", views.get_questions, name='question'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('vote/<int:question_id>', views.vote, name='vote'),
    path('results/<int:question_id>', views.results, name='results'),
]
