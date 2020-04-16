from django.forms import ModelForm
from .models import PaymentDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, ButtonHolder

class PaymentDetailsForm(ModelForm):

    class Meta:
        model = PaymentDetail
        fields = ('name','email', 'mobile', 'amount', 'Description')
        labels = {
            'name' : "Name",
            'email': "Email Id",
            'mobile': "Contact Number",
            'amount': "Amount",
            'Description' : "Description"
        }
        
    helper = FormHelper()
    helper.form_class = 'form_group'
    helper.form_method = 'post'
    helper.layout = Layout(
        Field('name', css_class='form-control'),
        Field('email', css_class='form-control'),
        Field('mobile', css_class='form-control'),
        Field('amount', css_class='form-control'),
        Field('Description', css_class='form-control'),
        Submit('Submit', 'Submit', css_class="btn btn-primary"),
    )