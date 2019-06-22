from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import bank_details
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
def index(request):
	# return HttpResponse('Hello from Python!')
	return render(request, "index.html")


class bank_name_city_view(APIView):
	permission_classes = (IsAuthenticated,)

	@csrf_exempt
	def get(self, request):
		try:
			bank_name = "None"
			city = "None"
			offset = 0
			limit = 1
			if request.GET.get("bank_name") != None:
				bank_name = request.GET.get("bank_name")
			if request.GET.get("city") != None:
				city = request.GET.get("city")
			if request.GET.get("offset") != None:
				offset = request.GET.get("offset")
			if request.GET.get("limit") != None:
				limit = request.GET.get("limit")
			bank_detail_dict = {}
			query = "SELECT * FROM public.bank_details where bank_name = '{0}' and city = '{1}' LIMIT {2} OFFSET {3}".format(str(bank_name),str(city),str(limit),str(offset))
			print(query)
			for bank in bank_details.objects.raw(query):
				bank_detail_dict[bank.ifsc] = {"ifsc" : bank.ifsc,"bank_id":bank.bank_id,"branch":bank.branch,"address": bank.address,"city":bank.city,"district":bank.district,"state":bank.state,"bank_name":bank.bank_name}
			
			return JsonResponse({"bankbranch":bank_detail_dict})
		except Exception as e:
			return JsonResponse({"error":str(e)})

class ifsc_view(APIView):
	permission_classes = (IsAuthenticated,)

	@csrf_exempt
	def get(self, request):
		try:
			ifsc = "None"
			city = "None"
			offset = 0
			limit = 1

			if request.GET.get("ifsc") != None:
				ifsc = request.GET.get("ifsc")
			if request.GET.get("offset") != None:
				offset = request.GET.get("offset")
			if request.GET.get("limit") != None:
				limit = request.GET.get("limit")

			bank_detail_dict = {}
			query = "SELECT * FROM public.bank_details where ifsc = '{0}'  LIMIT {1} OFFSET {2}".format(str(ifsc),str(limit),str(offset))
			print(query)
			for bank in bank_details.objects.raw(query):
				bank_detail_dict[bank.ifsc] = {"ifsc" : bank.ifsc,"bank_id":bank.bank_id,"branch":bank.branch,"address": bank.address,"city":bank.city,"district":bank.district,"state":bank.state,"bank_name":bank.bank_name}
			return JsonResponse({"result":bank_detail_dict})
		except Exception as e:
			return JsonResponse({"error":str(e)})




