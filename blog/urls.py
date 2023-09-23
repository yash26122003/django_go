from django.urls import path
from .views import PostListView
from . import views


urlpatterns = [
   
    path('', PostListView.as_view(),name="blog-home"),
    path('hello/', views.login,name="hi-login"),
    path('about/', views.about,name="bog-about")

]