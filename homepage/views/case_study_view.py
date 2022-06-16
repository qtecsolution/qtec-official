from django.shortcuts import render
from django.views import View


class CaseStudyDetails(View):

    def get(self, request, slug):
        return render(request, 'case_study.html')