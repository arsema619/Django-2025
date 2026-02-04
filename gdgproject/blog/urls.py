from django.urls import path
from .views import hello_blog, WelcomeView, all_posts

urlpatterns = [
    path('', hello_blog, name='root'),                # <-- root URL
    path('home/', hello_blog, name='home'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('posts/', all_posts, name='all_posts'),
]
