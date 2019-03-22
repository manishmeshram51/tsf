from django.urls import path,include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment_process',views.payment_process, name='payment_process'),
    
    path('payment_done/', TemplateView.as_view(template_name= "myapp/payment_done.html"), name='payment_done'),

    path('payment_canceled/', TemplateView.as_view(template_name= "myapp/payment_canceled.html"), name='payment_canceled'),  
]
