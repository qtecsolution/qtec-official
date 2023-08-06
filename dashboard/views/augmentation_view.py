from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from dashboard.models import STATUS_TYPE, AugmantationBudget, AugmentationService, ServiceDetailsProject
from django.views import View
from django.contrib import messages


class AugmentationServicesView(View):
    def get(self, request):
        augmentation_services = AugmentationService.objects.all()
        context = {
            "augmentation_services" : augmentation_services,
            "status": STATUS_TYPE
        }
        return render(request, 'augmentation_service/augmentation_service.html', context)

    def post(self, request):
        if request.resolver_match.url_name == "augmentation_service_status_change_url":
            obj = AugmentationService.objects.get(id=request.POST.get('id'))
            obj.status = request.POST.get('status')
            obj.save()
            return JsonResponse({})
        if request.resolver_match.url_name == "delete_augmentation_url":
            request_id = request.POST.get('id')
            AugmentationService.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Data deteted successful!')
            return redirect('dashboard:augmentation_services_url')
        
        