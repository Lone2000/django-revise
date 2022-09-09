from unittest import result
from django.urls import path
from . import views

#Creating URL Patterns To Call App View's



app_name = 'polls'
urlpatterns = [
    # Example :/polls/
    path('', views.index, name="index"),

    # Example; polls/5
    path('<int:question_id>/', views.detail, name='detail'),

    # Example: polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),

    # Example: polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

    #Example: polls/celeb
    path('celeb/', views.celeb, name='celeb'),

    #Example: polls/celeb/1
    path('celeb/<int:celeb_id>', views.celeb_detail, name='celeb_detail'),

] 

