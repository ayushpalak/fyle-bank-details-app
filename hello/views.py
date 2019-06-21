from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import bank_details
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.filter().values()
#     print(greetings)

#     return JsonResponse({"greetings": list(greetings)},safe=False)


@csrf_exempt
def bank_name_city(request):
	try:
		received_json_data = json.loads(request.body.decode())
		bank_name = received_json_data["bank_name"]
		city = received_json_data["city"]
		offset = received_json_data["offset"]
		limit = received_json_data["limit"]
		bank_branch = []
		query = 'SELECT * FROM public.bank_details where bank_name = {0} and city = {1} LIMIT {2} OFFSET {3}'.format(str(bank_name),str(city),str(limit),str(offset))
		print(query)
		for bank in bank_details.objects.raw(query):
			bank_branch.append(bank.bank_branch)

		return JsonResponse({"bankbranch":bank_branch})
	except Exception as e:
		return JsonResponse({"error":str(e)})

@csrf_exempt
def ifsc(request):
	try:
		received_json_data = json.loads(request.body.decode())
		ifsc = received_json_data["ifsc"]
		offset = received_json_data["offset"]
		limit = received_json_data["limit"]
		bank_branch = []
		query = 'SELECT * FROM public.bank_details where ifsc = {0}  LIMIT {1} OFFSET {2}'.format(str(ifsc),str(limit),str(offset))
		for bank in bank_details.objects.raw(query):
			bank_branch.append(bank.bank_branch)
		return JsonResponse({"result":result})
	except Exception as e:
		return JsonResponse({"error":str(e)})





