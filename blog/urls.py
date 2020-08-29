from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_view, name='home_view'),
    path('listing', views.post_list, name='post_list'),
    path('practices', views.practice_list, name='practice_list'),
    path('practices/<int:pk>/', views.practice_detail, name='practice_detail'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('news', views.news_page, name='news_page'),
    path('overview', views.overview_page, name='overview_page'),
    path('about', views.about_page, name='about_page'),
    path('blog', views.practitioner_blog, name='practitioner_blog'),
]



##### NOTES: #####
# - Perhaps change the <int:> with a string later down the road to show the practice name