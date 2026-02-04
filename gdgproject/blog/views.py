from django.http import HttpResponse
from django.views import View   # import View for CBV
from .models import Post        # import Post model

# Function-Based View (FBV)
def hello_blog(request):
    return HttpResponse("Hello Blog")

# Class-Based View (CBV)
class WelcomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django CBV")

# Function-Based View that returns all Post titles
def all_posts(request):
    # Fetch all posts from database
    posts = Post.objects.all()
    
    # Extract titles
    titles = [post.title for post in posts]
    
    # Join titles into a string
    response_text = ", ".join(titles)
    
    return HttpResponse(response_text)

