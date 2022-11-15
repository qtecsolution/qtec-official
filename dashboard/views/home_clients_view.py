from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from dashboard.models import ClientImage, HomeClients



class HomeClientsView(View):
    def get(self, request):
        home_clients = HomeClients.objects.first()
       
        context = {
            'home_clients': home_clients
        }
        return render(request, 'home-client/home-clients.html', context)

    def post(self, request):
        if request.resolver_match.url_name == "home_clients_image_url":
            home_clients = HomeClients.objects.first()
            request_id = request.POST.get('id')
            home_clients.clent_image.remove(request_id)
            ClientImage.objects.get(id=request_id).delete()
            return JsonResponse({})
        
        else:
            file = request.FILES
            data = request.POST
            home_clients = HomeClients.objects.first()
            for item in file:
                obj = ClientImage()
                obj.image = file[item]
                obj.save()
                home_clients.clent_image.add(obj.id)
            home_clients.title = data.get('title')
            home_clients.save()
            return redirect('dashboard:home_clients_url')
        
      
