from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]



##### NOTES: #####
# - Perhaps change the <int:> with a string later down the road to show the practice name