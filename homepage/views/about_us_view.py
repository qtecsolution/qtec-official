from django.shortcuts import render
from django.views import View

from dashboard.models import LegalTeamMembers, OurGallery, TeamMembers, YouTubeVideo


class AboutUsView(View):

    def get(self, request):
        members = TeamMembers.objects.order_by('priority').values()
        legal_members = LegalTeamMembers.objects.order_by('priority').values()
        our_gallery = OurGallery.objects.order_by('priority').values()
        video_link = YouTubeVideo.objects.filter(
            page=YouTubeVideo.ABOUT_US, display=True).first()
        context = {
            "members": members,
            "legal_members": legal_members,
            "title": "About Us",
            "our_gallery": our_gallery,
            "video_link": video_link,

        }

        return render(request, 'about_us.html', context)
