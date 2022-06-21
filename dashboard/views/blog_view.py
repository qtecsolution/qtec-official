from multiprocessing import context
from django import views
from django.shortcuts import render
from django.views import View
from django.contrib import messages

from dashboard.models import Blog, BlogAuthor, BlogCategory, HandleBlog
from django.contrib.auth.models import User



class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.order_by("-id").all()
        blog_author = BlogAuthor.objects.values('id','name')
        blog_category = BlogCategory.objects.values('id','name')
        context = {
            "blogs" : blogs,
            'blog_author' :blog_author,
            'blog_category' : blog_category
        }
        return render(request, 'blog.html', context)
    def post(self, request):
        data =request.POST
        if request.resolver_match.url_name == "save_blog_url":
            blog_author = data.get('blog_author')
            blog_category = data.get('blog_category')
            title = data.get('title')
            description = data.get('description')
            image = request.FILES.get('image')
            tags = data.get('tags')
            created_at = data.get('created_at')
            updated_at = data.get('updated_at')
            if not blog_author or not description or not tags:
                 messages.error(request, 'Invalid input!')
            else:
                blog_object = Blog()
                blog_object.blog_author_id = blog_author
                blog_object.blog_category_id = blog_category
                blog_object.title = title
                blog_object.description = description
                blog_object.tags = tags
                blog_object.image = image
                blog_object.created_at = created_at
                blog_object.updated_at = updated_at
                blog_object.save()
                messages.success(request, 'Data save successful!')
            return self.get(request)
            
        if request.resolver_match.url_name == "edit_blog_url":
            blog_author = data.get('blog_author')
            blog_category = data.get('blog_category')
            title = data.get('title')
            description = data.get('description')
            image = request.FILES.get('image')
            tags = data.get('tags')
            created_at = data.get('created_at')
            updated_at = data.get('updated_at')
            if not blog_author or not description or not tags:
                 messages.error(request, 'Invalid input!')
            else:
                request_id = data.get('id')
                blog_object = Blog.objects.filter(id=request_id).first()
                blog_object.blog_author_id = blog_author
                blog_object.blog_category_id = blog_category
                blog_object.title = title
                blog_object.description = description
                blog_object.tags = tags
                if image:
                    blog_object.image = image
                if created_at:
                    blog_object.created_at = created_at
                if updated_at:
                    blog_object.updated_at = updated_at
                blog_object.save()
                messages.success(request, 'Data updated successful!')

            return self.get(request)
        if request.resolver_match.url_name == "delet_blog_row_url":
            request_id = data.get('id')
            blog = Blog.objects.filter(id=request_id).first().delete()
            return self.get(request)
    
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
        top_4_blog = request.POST.getlist('top_4_blog')
        
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
       
        return self.get(request)

class BlogAuthorView(View):
    def get(self, request):
        blogs = Blog.objects.values('id','title')
        blog_author = BlogAuthor.objects.values()
    
        context = {
            'blog_author': blog_author,
            'blogs': blogs,
        }
        return render(request, 'blog_author.html', context)

    def post(self, request):
        data =request.POST
        if request.resolver_match.url_name == "save_blog_blog_author_url":
            blog_author = BlogAuthor()
            blog_author.name = data.get('name')
            blog_author.qualification = data.get('qualification')
            blog_author.image = request.FILES.get('image')
            blog_author.save()
            messages.success(request, 'Data save successful!')
            return self.get(request)
        if request.resolver_match.url_name == "delete_blog_blog_author_url":
            request_id = data.get('id')
            BlogAuthor.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Delete successful!')
            return self.get(request)
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
            return self.get(request)
            BlogCategoryView
class BlogCategoryView(View):
        def get(self, request):
            blog_category = BlogCategory.objects.values('id','name')
        
            context = {
                'blog_category': blog_category,
            }
            return render(request, 'blog_category.html', context)

        def post(self, request):
            data =request.POST
            if request.resolver_match.url_name == "save_blog_category_url":
                blog_category = BlogCategory()
                print("data.get('name')::::",data)
                blog_category.name = data.get('name')
                blog_category.save()
                messages.success(request, 'Data save successful!')
                return self.get(request)
            if request.resolver_match.url_name == "delete_blog_blog_category_url":
                request_id = data.get('id')
                BlogCategory.objects.filter(id=request_id).first().delete()
                messages.success(request, 'Delete successful!')
                return self.get(request)
            if request.resolver_match.url_name == "edit_blog_blog_category_url":
                request_id = data.get('id')
                blog_category = BlogCategory.objects.filter(id=request_id).first()
                blog_category.name = data.get('name')
                blog_category.save()
                messages.success(request, 'Data updated successful!')
                return self.get(request)
                BlogCategoryView
