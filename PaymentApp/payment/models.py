from django.db import models
from jsonfield import JSONField
import uuid
# Create your models here.
class Base(models.Model):
# base class  used to activate
# deactivate the related objects
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


PAYMENT_TYPE = ((2,"Full_Payment"),(1,"Partial_Sattlement"),(0,"Advance_Pay"))
class PaymentDetail(Base):
# payment details store
# name,email,PayType ,amount
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    Description = models.CharField(max_length=100, default="Payment")
    amount = models.PositiveIntegerField()
    email = models.EmailField(max_length=250)
    mobile = models.PositiveIntegerField(range(6000000000, 9999999999), default = 9999999999)

    def __str__(self):
        return self.email

PAYMENT_STATUS = ((2,"Success"),(1,'Pending'),(0,'Failed'))
class RazorpayResponse(Base):
# to store razorpay response
# with relationship of payment details
# object
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    response = JSONField()
    status = models.CharField(max_length=2,choices=PAYMENT_STATUS)
    relation = models.ForeignKey(PaymentDetail,on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.relation.email +" "+ str(self.id)