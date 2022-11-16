from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from dashboard.models import WhatPeopleSay
from django.contrib import messages



class WhatPeopleSayView(View):
    
    def get(self, request,id=None):
        
        if request.resolver_match.url_name == "create_what_people_say_url":
            return render(request, 'what-people-say/create_what_people_say.html')
        if request.resolver_match.url_name == "update_what_people_say_url":
            what_people_say = WhatPeopleSay.objects.get(id=id)
            return render(request, 'what-people-say/update_what_people_say.html',{'what_people_say': what_people_say})
        else:
            what_people_say = WhatPeopleSay.objects.values().order_by('priority')
        
            context = {
                'what_people_say': what_people_say
            }
            return render(request, 'what-people-say/what_people_say.html', context)

    def post(self, request,id=None):
        data = request.POST
        file = request.FILES
        if request.resolver_match.url_name == "create_what_people_say_url":
            what_people_say = WhatPeopleSay()
            what_people_say.name = data.get('name')
            what_people_say.image = file.get('image')
            what_people_say.designation = data.get('designation')
            what_people_say.description = data.get('description')
            what_people_say.priority = data.get('priority')
            what_people_say.save()
            messages.success(request, 'Data Saved successful!')
            return redirect('dashboard:what_people_say_url')
        if request.resolver_match.url_name == "delete_what_people_say_url":
            request_id = request.POST.get('id')
            WhatPeopleSay.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Data deteted successful!')
            return redirect('dashboard:what_people_say_url')
        if request.resolver_match.url_name == "update_what_people_say_url":
            what_people_say = WhatPeopleSay.objects.get(id=id)
            what_people_say.name = data.get('name')
            image = file.get('image')
            if image:
                what_people_say.image = image
            what_people_say.designation = data.get('designation')
            what_people_say.description = data.get('description')
            what_people_say.priority = data.get('priority')
            what_people_say.save()
            messages.success(request, 'Data Updated successful!')
            return redirect('dashboard:what_people_say_url')
          
        
        # else:
        #     file = request.FILES
        #     data = request.POST
        #     home_clients = HomeClients.objects.all()
        #     if home_clients.exists():
        #         home_clients = home_clients.first()
        #     else:
        #         home_clients = HomeClients()
        #     home_clients.title = data.get('title')
        #     home_clients.save()
        #     for item in file:
        #         obj = ClientImage()
        #         obj.image = file[item]
        #         obj.save()
        #         home_clients.clent_image.add(obj.id)
            
        #     return redirect('dashboard:home_clients_url')
        
      
