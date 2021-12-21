from django.urls import re_path
from BlogApp import views

#url is depreciated in django 4.0, import path and re_path instead
urlpatterns = [
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^post/?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    re_path(r'^post/?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^post/?P<pk>\d+/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    re_path(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),

]