
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('speaking/', views.speaking,name='speaking'),
    path('speaking/create_conversations/', views.create_conversations,name='create_conv'),
    path('speaking/adj/', views.adj_detail,name='adj'),
    path('speaking/slang/', views.slang_detail,name='slang'),
    path('speaking/usefull_sentences/', views.us_detail,name='usefulse'),
    path('speaking/phrasalVerbes/', views.pv_detail,name='phver'),
    path('speaking/commonWords/', views.cw_detail,name='commonWords'),
    path('speaking/create_story/', views.create_story,name='create_story'),
    path('conversation/<slug:slug>/', views.conversation_detail,name='conversation'),
    path('conversation/<slug:slug>/<str:id>/', views.update_conversation,name='conversation'),
    path('vocabulary/<slug:slug>/<str:id>/', views.update_vocabulary,name='vocabulary'),
    
    path('delete/<slug:slug>/<str:id>/', views.delete_conversation,name='delete'),
    path('delete_vocabulary/<slug:slug>/<str:id>/', views.delete_vocabulary,name='delete_v'),
    
    path('vocabulary/<slug:slug>/', views.vocabulary_detail,name='vocabulary'),
    path('story/<slug:slug>/', views.story_detail,name='story'),
    path('blog/<slug:slug>/', views.blog_view,name='blog'),
    path('search/', views.search_view,name='search'),
]
