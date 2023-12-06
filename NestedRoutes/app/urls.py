
from app import views
from django.urls import path, include


posts_patterns = [
    path("popular", views.popular),
    path("new", views.new),
    path("allposts", views.all_posts),
    ]

urlpatterns = [
    path("", views.index),
    path("posts/", include(posts_patterns)),
    path("about/", views.about),
    path("contacts/", views.contacts),
    path("error", views.error),
    path('access/', views.access),
    path('access/<str:login>/', views.access),
    path('access/<str:login>/<str:password>/', views.access),
    path("posts/likesandcom/<int:post>", views.get_likes_com),
    path('json/', views.js_file),
    path('json/<str:name>/', views.js_file),
    path('json/<str:name>/<int:age>/', views.js_file),
    path('set', views.set),
    path('get', views.get),
]