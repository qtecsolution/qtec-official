from django.shortcuts import render
from django.views import View

from dashboard.models import CurrentOpportunities


class CareerView(View):

    def get(self, request):
        careers = CurrentOpportunities.objects.all()
        context = {
            'title': "Career",
            'careers': careers
        }
        return render(request, 'career_page.html', context)