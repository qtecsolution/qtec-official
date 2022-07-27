from django.shortcuts import render
from django.views import View

from dashboard.models import OurGallery, TeamMembers


class AboutUsView(View):

    def get(self, request):
        members = TeamMembers.objects.order_by('priority').values()
        our_gallery = OurGallery.objects.order_by('priority').values()
        context = {
            "members" : members,
            "title": "About Us",
            "our_gallery" : our_gallery,

        }

        return render(request, 'about_us.html', context)