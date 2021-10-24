import sys
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Double
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase


class SoapService(ServiceBase):
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def hello(self, name):
        return 'Hello, {}'.format(name)

    @rpc(Double(nillable=False), Double(nillable=False), _returns=Double)
    def sum(ctx, a, b):
        return a + b
    
    @rpc(Double(nillable=False),Double(nillable=False), _returns=Double )        
    def prod(self, a, b):
        return a*b

    @rpc(Double(nillable=False),Double(nillable=False), _returns=Double )        
    def div(self, a, b):
        try:
            res= a/b
            
        # except ZeroDivisionError as e :
        #     print("Unexpected error:", e)
        # except :
        #     print("Error : ",sys.exc_info()[0])
        # except Exception as e :
        #     print(e.message)
        except :
            print('you are trying to divide by zero')
        return res;
#création d'une instance
soap_app = Application(
    [SoapService],
    tns='isg.soa.bis.calculator',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)


