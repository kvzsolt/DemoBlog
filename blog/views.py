from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post
from django.views import generic
from django.template.defaultfilters import slugify


"""
@csrf_exempt
def index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        data = Post.objects.filter(title__icontains=search)
    else:
        data = Post.objects.all()
    if request.method == 'POST':
        title = request.POST.get('post-title')
        content = request.POST.get('post-text')
        obj = Post()
        obj.title = title        
        obj.content = content
        obj.created_on
        obj.save()
    return render(request, 'index.html',{'data': data})
"""


class PostList(generic.ListView):
    queryset = Post.objects.filter().order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'data'

    def post(self, request, *args, **kwargs):
        title = request.POST.get('post-title')
        content = request.POST.get('post-text')
        obj = Post()
        obj.title = title
        obj.slug = slugify(title)
        obj.content = content
        obj.created_on
        obj.save()
        data = self.get_queryset()
        return render(request, 'index.html',{'data':data})

    def get_queryset(self, *args, **kwargs):
        data = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('search')
        if query:
            return data.filter(title__icontains=query)
        return data


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
