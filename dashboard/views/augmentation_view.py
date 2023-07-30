from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from dashboard.models import STATUS_TYPE, AugmantationBudget, AugmentationService, ServiceDetailsProject
from django.views import View


class AugmentationServicesView(View):
    def get(self, request):
        augmentation_services = AugmentationService.objects.all()
        context = {
            "augmentation_services" : augmentation_services,
            "status": STATUS_TYPE
        }
        return render(request, 'augmentation_service/augmentation_service.html', context)

    def post(self, request):
        obj = AugmentationService.objects.get(id=request.POST.get('id'))
        obj.status = request.POST.get('status')
        obj.save()
        return JsonResponse({})