from django.shortcuts import render
from django.views import View

from dashboard.models import HandleBlog, Blog


class BlogsView(View):

    def get(self, request):
        handle_blog= HandleBlog.objects.first()
        top_4_blog = handle_blog.top_4_blog.select_related('blog_author').select_related('blog_category').all()
        random_blog = Blog.objects.exclude(id__in=top_4_blog.values_list('id', flat= True)).order_by('?')
        context = {
            'highlight_blog': handle_blog.highlight_blog,
            'top_4_blog': top_4_blog,
            'random_blog': random_blog
        }
        return render(request, 'blog/blog.html', context)


class BlogDetails(View):

    def get(self, request, category_slug, slug):
        blog = Blog.objects.get(slug= slug)
        random_blog = Blog.objects.filter(blog_category__slug= category_slug).exclude(id= blog.id).select_related('blog_author').select_related('blog_category')
        random_blog = random_blog[:5] if random_blog.count() > 4 else random_blog
        return render(request, 'blog/blog_details.html' ,{'blog': blog, 'random_blog': random_blog})