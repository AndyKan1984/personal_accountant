from json import JSONEncoder
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from webapp.models import User, Expense, Income
from datetime import datetime

# Create your views here.


@csrf_exempt
def new_expense(request):
    token = request.POST['token']
    try:
        user = User.objects.filter(token__token=token).get()
    except User.DoesNotExist:
        return HttpResponse(status=403)

    expense = Expense.objects.create(
        user=user,
        time=datetime.now(),
        amount=request.POST['amount'],
        note=request.POST['note']
    )

    print(expense)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def new_income(request):
    token = request.POST['token']
    try:
        user = User.objects.filter(token__token=token).get()
    except User.DoesNotExist:
        return HttpResponse(status=403)

    Income.objects.create(
        user=user,
        time=datetime.now(),
        amount=request.POST['amount'],
        note=request.POST['note']
    )

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
