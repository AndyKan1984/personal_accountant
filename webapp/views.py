from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


@csrf_exempt
def new_expense(request):
    print(request.POST)
    return JsonResponse({
        'status': 'ok'
    })
