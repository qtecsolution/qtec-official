from email import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from dashboard.models import WhatProjectHaveWeDone
from django.contrib import messages


class AlreadyDoneView(View):

    def get(self, request):
        what_Done = WhatProjectHaveWeDone.objects.order_by("-id").values()
        context = {
            "what_Done" : what_Done,
        }
        return render(request, 'already_done.html', context)
    def post(self, request):
        data = request.POST
        if request.resolver_match.url_name == "delet_what_done_url":
            request_id = request.POST.get('id')
            what_Done = WhatProjectHaveWeDone.objects.filter(id=request_id).delete()
            messages.success(request, 'Delete successful')
            return self.get(request)
            
        if request.resolver_match.url_name == "save_what_done_url":
            what_Done = WhatProjectHaveWeDone()
            name = data.get('name')
            technology = data.get('technology')
            image =  request.FILES.get('image')
            print("image", image)
            if not name or not technology or not image:
                messages.error(request, 'Invalid input!')
              
            else:
                what_Done.name = name
                what_Done.technology = technology
                what_Done.image = image
                what_Done.save()
                messages.success(request, 'Data save successful!')
            return self.get(request)


            

        