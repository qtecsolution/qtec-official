from datetime import date, datetime
from multiprocessing import context
from django import views
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from dashboard.models import Blog, BlogAuthor, BlogCategory, HandleBlog
from django.contrib.auth.models import User

from dashboard.utils import SlugGeneratorMixin



class BlogView(View):
    def get(self, request,id=None):
        if request.resolver_match.url_name == "save_blog_url":
            blog_author = BlogAuthor.objects.values('id','name')
            blog_category = BlogCategory.objects.values('id','name')
            context = {
                'blog_author' :blog_author,
                'blog_category' : blog_category
            }
            return render(request, 'blogs/blog_create.html', context)

        if request.resolver_match.url_name == "edit_blog_url":
            blog = Blog.objects.filter(id=id).first()
            blog_author = BlogAuthor.objects.values('id','name')
            blog_category = BlogCategory.objects.values('id','name')
            context = {
                'blog_author' :blog_author,
                'blog_category' : blog_category,
                'blog': blog
            }
            return render(request, 'blogs/blog_update.html', context)
        
        else:
            blog = Blog.objects.order_by("-id").all()
            blog_author = BlogAuthor.objects.values('id','name')
            blog_category = BlogCategory.objects.values('id','name')
            context = {
                "blogs" : blog,
                'blog_author' :blog_author,
                'blog_category' : blog_category
            }
            return render(request, 'blogs/blog.html', context)
 

    def post(self, request,id=None):
        data =request.POST
        
        if request.resolver_match.url_name == "save_blog_url":
            self.data_save(request,flag='created')
            messages.success(request, 'Data Saved successful!')

            return redirect('dashboard:blog_blog_list_url')
            
        if request.resolver_match.url_name == "edit_blog_url":
            self.data_save(request,flag='edit')
            messages.success(request, 'Data updated successful!')

            return redirect('dashboard:blog_blog_list_url')
        if request.resolver_match.url_name == "delete_blog_row_url":
            request_id = data.get('id')
            Blog.objects.filter(id=request_id).first().delete()

            return redirect('dashboard:blog_blog_list_url')
        if request.resolver_match.url_name == "display_blog_row_url":
            request_id = data.get('id')
            blog = Blog.objects.get(id=request_id)
            blog.display = False if blog.display == True else True
            blog.save()

            return JsonResponse({})  
            
    @staticmethod
    def data_save(request,flag=None):
        data =request.POST
        request_id = data.get('id')
        blog_object = Blog.objects.filter(id=request_id)
        if blog_object.exists():
            obj = blog_object.first()
        else:
            obj = Blog()
        obj.blog_author_id = data.get('blog_author')
        obj.blog_category_id = data.get('blog_category')
        obj.description = data.get('description')
        obj.og_description = data.get('og_description')
        image = request.FILES.get('image')
        title = data.get('title')
        if image:
            obj.image = image
        obj.tags = data.get('tags')
        if flag=='created':
            obj.created_at =  date.today()
            obj.title = title
        else:
            if obj.title != title:
                obj.title = title
                slug_object = SlugGeneratorMixin()
                slug = slug_object.unique_slug_generator(obj)
                obj.slug = slug
            obj.updated_at =  date.today()
        obj.save()
    
class HandleBlogView(View):
    def get(self, request):
        blogs = Blog.objects.values('id','title')
        if HandleBlog.objects.exists():
            top_4_blog = HandleBlog.objects.first().top_4_blog.values_list('id',flat=True)
            highlight_blog = HandleBlog.objects.first().highlight_blog.id
        else:
            top_4_blog =""
            highlight_blog = ""
        context = {
            'blogs': blogs,
            'top_4_blog': top_4_blog,
            'highlight_blog':highlight_blog,
        }

        return render(request, 'handle_blog.html', context)

    def post(self, request):
        data = request.POST
        handle_blog = HandleBlog.objects.first()
        highlight_blog = data.get('highlight_blog')
        if HandleBlog.objects.exists():
            handle_blog = HandleBlog.objects.first()
            handle_blog.top_4_blog.clear()
        else:
            handle_blog = HandleBlog()
        handle_blog.highlight_blog = Blog.objects.filter(id=highlight_blog).first()
        handle_blog.save()
        top_4_blog = request.POST.getlist('top_4_blog')
        handle_blog.top_4_blog.add(*top_4_blog)
        messages.success(request, 'Data updated successful!')
       
        return redirect('dashboard:handle_blog_url')

class BlogAuthorView(View):
    def get(self, request):
        blogs = Blog.objects.values('id','title')
        blog_author = BlogAuthor.objects.values().order_by("-id")
    
        context = {
            'blog_author': blog_author,
            'blogs': blogs,
        }
    
        return render(request, 'blogs/blog_author.html', context)

    def post(self, request):
        data =request.POST
        if request.resolver_match.url_name == "save_blog_blog_author_url":
            blog_author = BlogAuthor()
            blog_author.name = data.get('name')
            blog_author.qualification = data.get('qualification')
            blog_author.image = request.FILES.get('image')
            blog_author.save()
            messages.success(request, 'Data save successful!')

            return redirect('dashboard:blog_blog_author_url')

        if request.resolver_match.url_name == "delete_blog_blog_author_url":
            request_id = data.get('id')
            BlogAuthor.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Delete successful!')

            return redirect('dashboard:blog_blog_author_url')

        if request.resolver_match.url_name == "edit_blog_blog_author_url":
            request_id = data.get('id')
            blog_author = BlogAuthor.objects.filter(id=request_id).first()
            blog_author.name = data.get('name')
            blog_author.qualification = data.get('qualification')
            image = request.FILES.get('image')

            if image:
                blog_author.image = image

            blog_author.save()
            messages.success(request, 'Data updated successful!')

            return redirect('dashboard:blog_blog_author_url')
class BlogCategoryView(View):
        def get(self, request):
            blog_category = BlogCategory.objects.values('id','name').order_by("-id")
        
            context = {
                'blog_category': blog_category,
            }
            return render(request, 'blogs/blog_category.html', context)

        def post(self, request):
            data =request.POST
            if request.resolver_match.url_name == "save_blog_category_url":
                blog_category = BlogCategory()
                blog_category.name = data.get('name')
                blog_category.save()
                messages.success(request, 'Data save successful!')

                return redirect('dashboard:blog_blog_category_url')

            if request.resolver_match.url_name == "delete_blog_blog_category_url":
                request_id = data.get('id')
                BlogCategory.objects.filter(id=request_id).first().delete()
                messages.success(request, 'Delete successful!')

                return redirect('dashboard:blog_blog_category_url')

            if request.resolver_match.url_name == "edit_blog_blog_category_url":
                request_id = data.get('id')
                blog_category = BlogCategory.objects.filter(id=request_id).first()
                blog_category.name = data.get('name')
                blog_category.save()
                messages.success(request, 'Data updated successful!')

                return redirect('dashboard:blog_blog_category_url')

            
            
