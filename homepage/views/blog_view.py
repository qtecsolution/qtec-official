from django.shortcuts import render
from django.views import View


class BlogsView(View):

    def get(self, request):
        return render(request, 'blog/blog.html')


class BlogDetails(View):

    def get(self, request, slug):
        return render(request, 'blog_details.html')