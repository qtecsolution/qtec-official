from multiprocessing import context
from django.shortcuts import render
from django.views import View

from dashboard.models import Technologies, TechnologyFeatures


class TechnologiesView(View):

    def get(self, request, slug):
        print("slug::::", slug)
        technologies = Technologies.objects.filter(slug=slug).first()
        features = TechnologyFeatures.objects.all()
        context = {
            "technologies" : technologies,
            "features" : features
        }
        return render(request, 'technology/technologies.html', context)

      