import sys
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase


class SoapService(ServiceBase):
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def hello(ctx, name):
        return 'Hello, {}'.format(name)

    @rpc(Integer(nillable=False), Integer(nillable=False), _returns=Integer)
    def sum(ctx, a, b):
        return int(a + b)
    
    @rpc(Integer(nillable=False),Integer(nillable=False), _returns=Integer )        
    def prod(ctx, a, b):
        return int(a*b);

    @rpc(Integer(nillable=False),Integer(nillable=False), _returns=Integer )        
    def div(ctx, a, b):
        try:
            res= int(a/b);
            
        # except ZeroDivisionError as e :
        #     print("Unexpected error:", e)
        # except :
        #     print("Error : ",sys.exc_info()[0])
        # except Exception as e :
        #     print(e.message)
        except :
            print('you are trying to divide by zero')
        return res;

soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)


