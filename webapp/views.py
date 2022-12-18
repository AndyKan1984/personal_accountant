from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from webapp.models import User, Expense
from datetime import datetime

# Create your views here.


@csrf_exempt
def new_expense(request):
    token = request.POST['token']
    user = None
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

    print(request.POST)
    print(expense)
    return JsonResponse({
        'status': 'ok'
    })
