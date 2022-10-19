from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from dashboard.models import OurGallery, Subscribe


class OurGalleryView(View):
    def get(self, request, id=None):
        if request.resolver_match.url_name == "save_our_gallery_url":
            return render(request, 'our_gallery/our_gallery_create.html')
        if request.resolver_match.url_name == "update_our_gallery_url":
            our_gallery = OurGallery.objects.filter(id=id).first()
            context = {
                "our_gallery" : our_gallery,
            }
            return render(request, 'our_gallery/update_gallery_create.html', context)
        else:
            our_gallery = OurGallery.objects.order_by('-priority')
            context = {
                "our_gallery" : our_gallery,
            }
            return render(request, 'our_gallery/our_gallery.html', context)
    def post(self, request, id=None):
        data = request.POST
        file = request.FILES
        if request.resolver_match.url_name == "update_our_gallery_url":
            gallery = OurGallery.objects.filter(id=id).first()
            gallery.title = data.get('title')
            gallery.description = data.get('description')
            primary_image = file.get('primary_image')
            if primary_image:
                gallery.primary_image = primary_image
            secondary_image = file.get('secondary_image')
            if secondary_image:
                gallery.secondary_image = secondary_image
            gallery.priority = data.get('priority')
            gallery.save()
            messages.success(request, 'Data Update successful!')
            return redirect('dashboard:our_gallery_url')
        if request.resolver_match.url_name == "delete_our_gallery_url":
            gallery = OurGallery.objects.filter(id=data.get('id')).first().delete()
            messages.success(request, 'Data Deleted successful!')
            return redirect('dashboard:our_gallery_url')
        else:
            gallery = OurGallery()
            gallery.title = data.get('title')
            gallery.description = data.get('description')
            gallery.primary_image = file.get('primary_image')
            gallery.secondary_image = file.get('secondary_image')
            gallery.priority = data.get('priority')
            gallery.save()
            messages.success(request, 'Data save successful!')
            return redirect('dashboard:our_gallery_url')