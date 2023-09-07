from django.shortcuts import render
from bloge.models.models import Post
from portyfolio.settings import get_sqlite3_location
# Create your views here.

def index(request):
    post = Post.objects.all
    template_name = 'bloge/home.html'
    context = {
        'post' : post,
        'get_sqlite3_location' : get_sqlite3_location('sqilite3')
        }
    return render(request, template_name, context)
