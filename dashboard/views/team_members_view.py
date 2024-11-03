from django.shortcuts import redirect, render
from django.views import View

from dashboard.models import LegalTeamMembers, TeamMembers
from django.contrib import messages


class TeamMembersView(View):
    def get(self, request, id = None):
        if request.resolver_match.url_name == "save_team_member_url":
            return render(request, 'team_members/team_members_create.html')
        if request.resolver_match.url_name == "update_team_member_url":
            member = TeamMembers.objects.filter(id=id).first()
            context = {
                "member" : member,
            }
            return render(request, 'team_members/team_member_update.html', context)
        else:
            team_members = TeamMembers.objects.order_by('priority').values()
            context = {
                "team_members" : team_members,
            }
            return render(request, 'team_members/team_members.html', context)

    def post(self, request, id=None):
        data = request.POST
        file = request.FILES
        if request.resolver_match.url_name == "delete_team_member_url":
            request_id = request.POST.get('id')
            TeamMembers.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Data deteted successful!')
            return redirect('dashboard:team_members_url')
            
        if request.resolver_match.url_name == "update_team_member_url":
            member = TeamMembers.objects.filter(id=id).first()
            member.name = data.get('name')
            image = file.get('image')
            if image:
                member.image = image
            member.designation = data.get('designation')
            member.github = data.get('github')
            member.linkedin = data.get('linkedin')
            member.instagram = data.get('instagram')
            member.gmail = data.get('gmail')
            member.priority = data.get('priority')
            member.save()
            messages.success(request, 'Data save successful!')
            return redirect('dashboard:team_members_url')
        else:
            member = TeamMembers()
            member.name = data.get('name')
            member.image = file.get('image')
            member.designation = data.get('designation')
            member.github = data.get('github')
            member.linkedin = data.get('linkedin')
            member.instagram = data.get('instagram')
            member.gmail = data.get('gmail')
            member.priority = data.get('priority')
            member.save()
            messages.success(request, 'Data save successful!')
            return redirect('dashboard:team_members_url')


class LegalTeamMembersView(View):
    def get(self, request, id = None):
        if request.resolver_match.url_name == "save_legal_member_url":
            return render(request, 'legal_members/team_members_create.html')
        if request.resolver_match.url_name == "update_legal_member_url":
            member = LegalTeamMembers.objects.filter(id=id).first()
            context = {
                "member" : member,
            }
            return render(request, 'legal_members/team_member_update.html', context)
        else:
            team_members = LegalTeamMembers.objects.order_by('priority').values()
            context = {
                "team_members" : team_members,
            }
            return render(request, 'legal_members/team_members.html', context)

    def post(self, request, id=None):
        data = request.POST
        file = request.FILES
        if request.resolver_match.url_name == "delete_legal_member_url":
            request_id = request.POST.get('id')
            LegalTeamMembers.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Data deteted successful!')
            return redirect('dashboard:legal_members_url')
            
        if request.resolver_match.url_name == "update_legal_member_url":
            member = LegalTeamMembers.objects.filter(id=id).first()
            member.name = data.get('name')
            image = file.get('image')
            if image:
                member.image = image
            member.designation = data.get('designation')
            member.github = data.get('github')
            member.linkedin = data.get('linkedin')
            member.instagram = data.get('instagram')
            member.gmail = data.get('gmail')
            member.priority = data.get('priority')
            member.save()
            messages.success(request, 'Data save successful!')
            return redirect('dashboard:legal_members_url')
        else:
            member = LegalTeamMembers()
            member.name = data.get('name')
            member.image = file.get('image')
            member.designation = data.get('designation')
            member.github = data.get('github')
            member.linkedin = data.get('linkedin')
            member.instagram = data.get('instagram')
            member.gmail = data.get('gmail')
            member.priority = data.get('priority')
            member.save()
            messages.success(request, 'Data save successful!')
            return redirect('dashboard:legal_members_url')

