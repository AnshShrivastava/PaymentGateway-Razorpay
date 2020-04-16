from django.contrib import admin
from .models import PaymentDetail, RazorpayResponse

admin.site.register(PaymentDetail)
admin.site.register(RazorpayResponse)
# Register your models here.
