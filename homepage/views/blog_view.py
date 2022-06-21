from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from dashboard.models import HandleBlog, Blog


class BlogsView(View):

    def get(self, request):
        handle_blog= HandleBlog.objects.first()
        handle_blog_exists = HandleBlog.objects.exists()
        top_4_blog = None
        random_blog = None
        highlight_blog = None
        if handle_blog_exists:
            top_4_blog = handle_blog.top_4_blog.select_related('blog_author').select_related('blog_category').all()
            random_blog = Blog.objects.exclude(id__in=top_4_blog.values_list('id', flat= True)).order_by('?')
            highlight_blog = handle_blog.highlight_blog
        context = {
            'handle_blog_exists' : handle_blog_exists,
            'title': 'Blog',
            'highlight_blog': highlight_blog,
            'top_4_blog': top_4_blog,
            'random_blog': random_blog
        }
        return render(request, 'blog/blog.html', context)
        



class BlogDetails(View):

    def get(self, request, category_slug, slug):
        blog = Blog.objects.get(slug= slug)
        random_blog = Blog.objects.filter(blog_category__slug= category_slug).exclude(id= blog.id).select_related('blog_author').select_related('blog_category')
        random_blog = random_blog[:5] if random_blog.count() > 4 else random_blog
        return render(request, 'blog/blog_details.html' ,{'blog': blog, 'random_blog': random_blog,
                                                          'abs_uri': request.build_absolute_uri,
                                                          'title': 'Blog Details'
                                                          })


class AllBlogView(View):

    def get(self, request):
        page = request.GET.get('page')
        blogs = Blog.objects.order_by('?')

        paginator = Paginator(blogs, settings.PER_PAGE)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'title': 'ALl Blogs'})