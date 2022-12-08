from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from an_app.models import PostModel


class DemoView(View):
    def get(self, request, post_id=None, create=False):

        if create:
            return render(request, 'posts/post_create.html')

        if post_id is None:
            return self.index(request)

        try:
            post = PostModel.objects.get(pk=post_id)
        except PostModel.DoesNotExist:
            raise Http404("Post does not exist")

        return render(request, 'posts/post_details.html', {'post': post})

    def index(self, request):
        try:
            posts = PostModel.objects.all()
        except PostModel.DoesNotExist:
            raise Http404("Post does not exist")
        return render(request, 'posts/index.html', {'posts': list(posts)})

    def post(self, request: HttpRequest, create=False):
        name = request.POST.get('name')
        content = request.POST.get('content')
        post = PostModel.objects.create(name=name, content=content)
        return redirect('an_app:post_view', post_id=f'{post.id}')


class MakeException(View):

    def get(self, request):
        return render(request, 'except/exception_portal.html', {'count': request.total_exception_count})

    def post(self, request):
        1 / 0


class TestNoRender(View):
    def get(self, request):
        return HttpResponse("Hello")
