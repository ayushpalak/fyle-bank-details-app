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
		bank_name = request.GET.get("bank_name")
		city = request.GET.get("city")
		offset = request.GET.get("offset")
		limit = request.GET.get("limit")
		bank_detail_dict = {}
		query = "SELECT * FROM public.bank_details where bank_name = '{0}' and city = '{1}' LIMIT {2} OFFSET {3}".format(str(bank_name),str(city),str(limit),str(offset))
		print(query)
		for bank in bank_details.objects.raw(query):
			bank_detail_dict[bank.ifsc] = {"ifsc" : bank.ifsc,"bank_id":bank.bank_id,"branch":bank.branch,"address": bank.address,"city":bank.city,"district":bank.district,"state":bank.state,"bank_name":bank.bank_name}
		
		return JsonResponse({"bankbranch":bank_detail_dict})
	except Exception as e:
		return JsonResponse({"error":str(e)})

@csrf_exempt
def ifsc(request):
	try:
		ifsc = request.GET.get("ifsc")
		offset = request.GET.get("offset")
		limit = request.GET.get("limit")
		bank_detail_dict = {}
		query = "SELECT * FROM public.bank_details where ifsc = '{0}'  LIMIT {1} OFFSET {2}".format(str(ifsc),str(limit),str(offset))
		print(query)
		for bank in bank_details.objects.raw(query):
			bank_detail_dict[bank.ifsc] = {"ifsc" : bank.ifsc,"bank_id":bank.bank_id,"branch":bank.branch,"address": bank.address,"city":bank.city,"district":bank.district,"state":bank.state,"bank_name":bank.bank_name}
		return JsonResponse({"result":bank_detail_dict})
	except Exception as e:
		return JsonResponse({"error":str(e)})





