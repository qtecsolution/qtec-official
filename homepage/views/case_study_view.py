from django.shortcuts import render
from django.views import View

from dashboard.models import CaseStudyDetails, WhatProjectHaveWeDone


class CaseStudyDetailsView(View):

    def get(self, request, slug):
        we_have_done = WhatProjectHaveWeDone.objects.get(slug= slug)
        case_study_details = we_have_done.case_study_details
        case_study_details = CaseStudyDetails.objects.filter(id=case_study_details.id, technology__view=True).first()
        print("case_study_details:::::::::", case_study_details)
        
        context = {
            'title': "Case Study",
            'we_have_done': we_have_done,
            'case_study_details': case_study_details
        }
        return render(request, 'case_study.html', context)