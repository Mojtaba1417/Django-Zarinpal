# Django-Zarinpal
# زرین پال

نحوه اتصال پروژه جنگو به زرین پال

## requirements
requests 2.29.0

 برای ارسال درخواست به زرین پال باید پکیج زیر را نصب کنید

```bash
pip install requests
```

## Usage
تنظیمات زیر را به پروژه خود اضافه کنید
```python
# sandbox
MERCHANT = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
SANDBOX = True
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'
ZP_API_REQUEST_URL = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY_URL = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY_URL = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
description = "www.comedur.com"
phone_number = '00000000000'
callback_url = 'http://127.0.0.1:8000/order/verify/'
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
