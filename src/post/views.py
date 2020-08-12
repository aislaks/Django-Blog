from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    post_list = Post.objects.all()
    template_name = 'post/list.html'
    context = {'post_list':post_list}
    return render(request, template_name, context)

def post_detail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    template_name = 'post/detail.html'
    context = {'post_detail':post_detail}
    return render(request, template_name, context)