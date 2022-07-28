from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post


@csrf_exempt
def index(request):
    data = Post.objects.all()
    if request.method == 'POST':
        title = request.POST.get('post-title')
        content = request.POST.get('post-text')
        obj = Post()
        obj.title = title
        obj.slug = title
        obj.content = content
        obj.created_on
        obj.save()
    return render(request, 'index.html',{'data': data})
