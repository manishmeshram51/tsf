# tsf
Paypal integration with Django

requirments:
1> pip install django
2> pip install django-paypal

Steps:
1.  Install django-paypal:

    pip install django-paypal

2.  Update settings.py file:

    INSTALLED_APPS = [
        'paypal.standard.ipn',
    ]

Add:

   PAYPAL_RECEIVER_EMAIL = 'XXXXX'
    PAYPAL_TEST = True

Note:
Write Email address of Receiver. 
“PAYPAL_TEST = True” means you want an Test API payment. You can write  "False" for Original payment API.

3.  Run command:

    python manage.py migrate 

4.  Now come to source code:

In url.py:

    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment_process/$', api_views.payment_process, name='payment_process' ),

    url(r'^payment_done/$', TemplateView.as_view(template_name= "pets/payment_done.html"), name='payment_done'),

    url(r'^payment_canceled/$', TemplateView.as_view(template_name= "pets/payment_canceled.html"), name='payment_canceled'),*

In views.py:

    from django.conf import settings
    from django.urls import reverse
    from django.shortcuts import render, get_object_or_404
    from paypal.standard.forms import PayPalPaymentsForm

    def payment_process(request):
        host = request.get_host()
        paypal_dict = {
       'business': settings.PAYPAL_RECEIVER_EMAIL ,
       'amount': ‘100’,
       'item_name': 'Item_Name_xyz',
       'invoice': ' Test Payment Invoice’,
       'currency_code': 'USD',
       'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
       'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
       'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
       }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'pets/payment_process.html', {'form': form })*

Note: Follow video tutorial for django-code given in reference.

In payment_process.html: 

     {{ form.render }}


For calling API you have request for /payment_process/. It will generate a button on HTML which calls PayPal API for transaction. Further process will be done on PayPal end, Login or Card Payment.**     

Reference:
(a) [https://django-paypal.readthedocs.io/en/stable/][1]
(b) [https://www.youtube.com/watch?v=Z5dBopZWOzo&t=417s][1]
(c) [https://overiq.com/django-paypal-integration-with-django-paypal]
