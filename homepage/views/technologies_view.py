from multiprocessing import context
from django.shortcuts import render
from django.views import View

from dashboard.models import Technologies, TechnologyFeatures


class TechnologiesView(View):

    def get(self, request, slug):
        technologies = Technologies.objects.get(slug=slug)
        features = TechnologyFeatures.objects.all()
        context = {
            'title': "Technologies",
            "technologies" : technologies,
            "features" : features
        }
        return render(request, 'technology/technologies.html', context)

      