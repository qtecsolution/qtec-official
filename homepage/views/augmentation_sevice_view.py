from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from homepage.forms.augmentation_service_form import AugmentationServiceForm
from dashboard.models import AugmantationBudget, AugmentationService, Service
import json
from django.views.decorators.csrf import csrf_exempt




# @csrf_exempt
# def augmentation_service(request):
#     if request.method == "POST":
#         response = json.loads(request.body)
#         print(response)
#         data = response['name']
#         print(data)
#         AugmentationService.objects.create(
#             name = response['name'],
#             company = response['company'],
#             phone = response['phone']
#         )
#     else:
#         return render(request,'staff_augmentation.html')
#     return HttpResponse("Okay")

def augmentation_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service_id = request.POST.get('service')
        budget_id = request.POST.get('budget')
        description = request.POST.get('description')



        AugmentationService.objects.create(
            name = name,
            company = company,
            phone = phone,
            email = email,
            services = Service.objects.get(pk=service_id),
            budget = AugmantationBudget.objects.get(pk=budget_id),
            description = description
        )
        return redirect('/')
    services = Service.objects.all()
    budgets = AugmantationBudget.objects.all()
    return render(request, 'staff_augmentation.html', {'services': services, 'budgets': budgets})
