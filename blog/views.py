from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post
from django.views import generic
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    print(post.id)
    is_liked = False
    if post.is_liked:
        post.is_liked = False
        post.save()
        is_liked = False
    else:
        post.is_liked = True
        post.save()
        is_liked = True
    """context = {
        'post': post,
        'is_liked': is_liked,
        'id': post.id
    }"""
    print(is_liked)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'is_liked': is_liked})



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
        obj.is_liked
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


