from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from dashboard.models import AugmentationService
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def augmentation_service(request):
    if request.method == "POST":
        response = json.loads(request.body)
        print(response)
        data = response['name']
        print(data)
        AugmentationService.objects.create(
            name = response['name'],
            company = response['company'],
            phone = response['phone']
        )
    else:
        return render(request,'staff_augmentation.html')
    return HttpResponse("Okay")
