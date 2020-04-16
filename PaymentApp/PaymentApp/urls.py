from django.conf.urls import url
from payment import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls ),
	url(r'pay$', views.StoreDetails.as_view(), name='pay'),
    url(r'^payment$', views.MyPayment.as_view(), name='payment'),
	]
