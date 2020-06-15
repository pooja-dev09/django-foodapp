from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views import View
import requests
import json
from .models import registration
# Create your views here.

class register(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status":"success"})

    def post(self, request, *args, **kwargs):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        name = body["name"]
        mobile = body["mobile"]
        email = body["email"]
        address = body["address"]
        d=registration(name=name,mobile=mobile,email=email,address=address)
        d.save()
        return JsonResponse({"myname":body["name"],"mobile":str(body["mobile"])})




