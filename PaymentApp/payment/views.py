from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from .forms import PaymentDetailsForm
from .models import PaymentDetail, RazorpayResponse
import requests

key = 'rzp_test_oNkHkLAvOKgI49'
secret = 'ytVxHWujw2lGDTNnX0ddtGH0'

def home(request):
    return render(request, 'home.html')

class StoreDetails(View):

    def get(self,request):
        template = 'store_user_details.html'
        form =PaymentDetailsForm()
        return render(request,template,locals())

    def post(self,request):
        form = PaymentDetailsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            template = 'get_user_details.html'
        else:
            form = PaymentDetailsForm()
            template = 'store_user_details.html'
        return render(request,template,locals())


@method_decorator(csrf_exempt, name='dispatch')
class MyPayment(View):
    def post(self,request):
        template = 'success.html'
        payment_id = request.POST.get('razorpay_payment_id')
        reference_obj = request.POST.get('payment_order_id')
        reference_obj_amount = request.POST.get('payment_order_amount')
        real_obj = PaymentDetail.objects.filter(uuid=reference_obj)
        print(real_obj)
        if int(real_obj[0].amount) == int(reference_obj_amount):
            url = 'https://api.razorpay.com/v1/payments/%s/capture' % str(payment_id)
            resp = requests.post(url, data={'amount':int(real_obj[0].amount)*100}, auth=(key, secret))
            if resp.status_code == 200:
                data = {"body": request.body, "content": resp.text}
                RazorpayResponse.objects.create(response=data,status=2,relation_id=int(real_obj[0].id))
                response = "Success"
            elif resp.status_code == 400:
                data = {"body": request.body, "content": resp.text}
                RazorpayResponse.objects.create(response=data,status=0,relation_id=int(real_obj[0].id))
                response = "Failed we will verify shortly"
            else:
                data = {"body": request.body, "content": resp.text}
                RazorpayResponse.objects.create(response=data,status=1,relation_id=int(real_obj[0].id))
                response = "Failed we will verify shortly"
        else:
            response = "This activity logged"
        return render(request,template,locals())
