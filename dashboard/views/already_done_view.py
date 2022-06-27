from django.shortcuts import redirect, render
from django.views import View

from dashboard.models import PROJECT_TYPE, CaseStudyDetails, KeyFeature, Technologies, WhatProjectHaveWeDone
from django.contrib import messages


class AlreadyDoneView(View):

    def get(self, request):
        technology = Technologies.objects.all()
        what_Done = WhatProjectHaveWeDone.objects.order_by("-id")

        context = {
            "what_Done" : what_Done,
            'technology': technology,
             "project_type" : PROJECT_TYPE
        }
        return render(request, 'already_done.html', context)

    def post(self, request):
        data = request.POST
        if request.resolver_match.url_name == "delete_what_done_url":
            request_id = request.POST.get('id')
            WhatProjectHaveWeDone.objects.filter(id=request_id).delete()
            messages.success(request, 'Delete successful')
            return redirect('dashboard:already_done_url')

        if request.resolver_match.url_name == "save_what_done_url":
            what_Done = WhatProjectHaveWeDone()
            what_Done.name = data.get('name')
            technology_id = data.getlist('technology')
            what_Done.image = request.FILES.get('image')
            what_Done.project_type = data.getlist('project_type')
            what_Done.save()
            what_Done.technology.add(*technology_id)
            messages.success(request, 'Data save successful!')
            return redirect('dashboard:already_done_url')

        if request.resolver_match.url_name == "edit_what_project_done_url":
            request_id = data.get('id')
            what_Done = WhatProjectHaveWeDone.objects.filter(id=request_id).first()
            what_Done.name = data.get('name')
            technology_id = data.getlist('technology')
            what_Done.project_type = data.getlist('project_type')
            image = request.FILES.get('image')
            if image:
                what_Done.image = image
            what_Done.save()
            what_Done.technology.clear()
            what_Done.technology.add(*technology_id)
            messages.success(request, 'Edit successful')
            return redirect('dashboard:already_done_url')


class CaseStudyEditView(View):

    def get(self, request, id):
        case_study = CaseStudyDetails.objects.filter(project_we_have_done=id).first()
        technologies = Technologies.objects.all()
        context = {
            "technologies" : technologies,
            "case_study" : case_study,
        }
        return render(request, 'partial/case_study_details.html', context)

    def post(self, request, id):
        data = request.POST
        file = request.FILES
        case_study_details = CaseStudyDetails.objects.filter(project_we_have_done=id).first()
        case_study_details.case_study_about = data.get('case_study_about')
        case_study_details.case_study_image = file.get('case_study_image')
        case_study_details.client_requirement = data.get('client_requirement')
        case_study_details.how_we_build_it = data.get('how_we_build_it')
        case_study_details.how_we_build_image = file.get('how_we_build_image')
        case_study_details.save()
        technology = data.getlist('technology')
        case_study_details.technology.clear()
        if technology:
            case_study_details.technology.add(*technology)
        messages.success(request, 'Case Study Details save successful')
        return redirect('dashboard:already_done_url')

class KeyFeatureView(View):
    def get(self, request, id= None):
        case_study = CaseStudyDetails.objects.filter(project_we_have_done=id).first()
        key_features = KeyFeature.objects.filter(case_study_details=case_study.id).all()
        context = {
            "key_features" : key_features,
            'id_': id
        }
        return render(request, 'partial/key_feature.html', context)
    def post(self, request, id = None):
        data = request.POST
        if request.resolver_match.url_name == "delete_key_feature_url":
            _id = data.get('already_done_id')
            KeyFeature.objects.filter(id=id).first().delete()
            return redirect('dashboard:key_feature_url', id=_id)
        else:
            key_features = KeyFeature()
            case_study = CaseStudyDetails.objects.filter(project_we_have_done=id).first()
            key_features.case_study_details = case_study
            key_features.title = data.get('title')
            key_features.description = data.get('description')
            key_features.image = request.FILES.get('image')
            key_features.save()
            return redirect('dashboard:key_feature_url', id=id)

