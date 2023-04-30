from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import json
import requests
from django .http import HttpResponse


# sandbox
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST_URL = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY_URL = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY_URL = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000
description = "www.comedur.com"
phone_number = '00000000000'
callback_url = 'http://127.0.0.1:8000/order/verify/'


class OrderPageView(View):
    def get(self, request):
        return render(request, 'order/orderpage.html')


class OrderPayView(View):
    def get(self, request):
        data = {
            'MerchantID': settings.MERCHANT,
            'Amount': amount,
            'Description': description,
            'CallbackURL': callback_url
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        res = requests.post(ZP_API_REQUEST_URL, data=data, headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                url = f"{ZP_API_STARTPAY_URL}{response['Authority']}"
                return redirect(url)
            pass
        else:
            print(res.json()['errors'])
            return HttpResponse(str(res.json()['errors']))


class VerifyPayView(View):
    def get(self, request):
        authority = request.GET['Authority']
        data = {
            'MerchantID': settings.MERCHANT,
            'Amount': amount,
            'Authority': authority
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        res = requests.post(ZP_API_VERIFY_URL, data=data, headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                return HttpResponse({'Status': response['Status'], 'RefID': response['RefID']})
            else:
                return HttpResponse({'Status': response['Status'], 'RefID': response['RefID']})
        return HttpResponse('پرداخت نا موفق')