from email import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from dashboard.models import APPLICENT_STATUS, ApplyForThisPosition, CurrentOpportunities


class CurrentOpportunitiesView(View):
    def get(self, request):
        current_opportunities = CurrentOpportunities.objects.all()
        applicent_type = APPLICENT_STATUS
        context = {
            "current_opportunities" : current_opportunities,
            "applicent_type" : applicent_type
        }
        return render(request, 'career_current_opportunities.html', context)

    def post(self, request):
        data = request.POST
        if request.resolver_match.url_name == "save_current_opportunities_url":
            current_opportunities = CurrentOpportunities()
            current_opportunities.title = data.get('title')
            current_opportunities.applicent_type = data.get('applicent_type')
            current_opportunities.number_of_vacancy = data.get('number_of_vacancy')
            current_opportunities.deadline = data.get('deadline')
            current_opportunities.description = data.get('description')
            current_opportunities.save()
            messages.success(request, 'Data save successful!')
            return self.get(request)
            
        if request.resolver_match.url_name == "current_opportunities_edit_url":
            request_id = data.get('id')
            current_opportunities = CurrentOpportunities.objects.filter(id=request_id).first()
            current_opportunities.title = data.get('title')
            current_opportunities.applicent_type = data.get('applicent_type')
            current_opportunities.number_of_vacancy = data.get('number_of_vacancy')
            deadline = data.get('deadline')
            if deadline:
                current_opportunities.deadline = deadline
            current_opportunities.description = data.get('description')
            current_opportunities.save()
            messages.success(request, 'Data Update successful!')
            return self.get(request)
            
        if request.resolver_match.url_name == "delet_current_opportunities_url":
            request_id = data.get('id')
            current_opportunities = CurrentOpportunities.objects.filter(id=request_id).first()
            current_opportunities.delete()
            messages.success(request, 'Delete successful!')
            return self.get(request)

 
class ApplyForThisPositionView(View):
    def get(self, request):
        positions = ApplyForThisPosition.objects.order_by("-id").all()
        context = {
            "positions" : positions,
        }
        return render(request, 'appply_for_this_position.html', context)
            
        
            



   