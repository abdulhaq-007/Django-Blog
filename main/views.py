from django.shortcuts import render

# Create your views here.
def home(request):
    post = Post.objects.all()
    context = {
        "post":post
    }
    return render(request, 'blue-index.html', context)