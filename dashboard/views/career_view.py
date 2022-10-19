from email import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from dashboard.models import ACTIVE_STATUS, APPLICENT_STATUS, APPLY_STATUS, ApplyForThisPosition, CurrentOpportunities


class CurrentOpportunitiesView(View):
    def get(self, request):
        current_opportunities = CurrentOpportunities.objects.all().order_by('-id')
        applicant_type = APPLICENT_STATUS
        status = ACTIVE_STATUS
        context = {
            "current_opportunities" : current_opportunities,
            "applicant_type" : applicant_type,
            "status": status
        }
        return render(request, 'career_current_opportunities.html', context)

    def post(self, request):
        data = request.POST
        if request.resolver_match.url_name == "save_current_opportunities_url":
            current_opportunities = CurrentOpportunities()
            current_opportunities.title = data.get('title')
            current_opportunities.applicant_type = data.get('applicant_type')
            current_opportunities.number_of_vacancy = data.get('number_of_vacancy')
            current_opportunities.deadline = data.get('deadline')
            current_opportunities.description = data.get('description')
            current_opportunities.image = request.FILES.get('image')
            current_opportunities.save()
            messages.success(request, 'Data save successful!')
            return redirect('dashboard:current_opportunities_url')
            
        if request.resolver_match.url_name == "current_opportunities_edit_url":
            request_id = data.get('id')
            current_opportunities = CurrentOpportunities.objects.filter(id=request_id).first()
            current_opportunities.title = data.get('title')
            current_opportunities.applicant_type = data.get('applicant_type')
            current_opportunities.number_of_vacancy = data.get('number_of_vacancy')
            image = image = request.FILES.get('image')
            if image:
                current_opportunities.image = image
            deadline = data.get('deadline')
            if deadline:
                current_opportunities.deadline = deadline
            current_opportunities.description = data.get('description')
            current_opportunities.save()
            messages.success(request, 'Data Update successful!')
            return redirect('dashboard:current_opportunities_url')
            
        if request.resolver_match.url_name == "delete_current_opportunities_url":
            request_id = data.get('id')
            current_opportunities = CurrentOpportunities.objects.filter(id=request_id).first()
            current_opportunities.delete()
            messages.success(request, 'Delete successful!')
            return redirect('dashboard:current_opportunities_url')
        if request.resolver_match.url_name == "change_status_current_opportunities_url":
            obj = CurrentOpportunities.objects.get(id=data.get('id'))
            obj.status = data.get('status')
            obj.save()
            return JsonResponse({})

 
class ApplyForThisPositionView(View):
    def get(self, request):
        positions = ApplyForThisPosition.objects.order_by("-id").all()
        context = {
            "positions" : positions,
            "apply_status" : APPLY_STATUS,
        }
        return render(request, 'apply_for_this_position.html', context)

    def post(self, request):
        data = request.POST
        if request.resolver_match.url_name == "apply_for_this_position_status_url":
            request_id = data.get('id')
            position = ApplyForThisPosition.objects.filter(id=request_id).first()
            position.status = data.get('status')
            position.save()
            return redirect('dashboard:apply_for_this_position_url')

        if request.resolver_match.url_name == "apply_for_this_position_delete_url":
            request_id = data.get('id')
            ApplyForThisPosition.objects.filter(id=request_id).first().delete()
            return redirect('dashboard:apply_for_this_position_url')
            
            
        
            



   