from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.

def home(request):
    return render(request,'myapp/index.html')

def payment_process(request):
    if request.method=='POST':
        
        em =  request.POST.get('email1')
        am =  request.POST.get('amount1')
        print("Email :",em)
        print("Amount :",am)
        host = request.get_host()
        paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL ,
        'amount': am ,
        'item_name': 'Donate',
        'invoice': '001',
        'currency_code': 'INR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, 'myapp/payment_process.html', {'form': form })    

