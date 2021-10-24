# soap_client.py
# coding=utf-8
try:
    from suds.client  import Client
    from suds.cache import NoCache

except ImportError:
     print('Cannot import SUDS')
my_client = Client('http://127.0.0.1:8000/calculator/?WSDL', cache=NoCache())
print (my_client)
your_name=input("What's your name ? ")
print ('Say hello: ', my_client.service.hello(your_name))
x=input("x = ")
y=input("y = ")
print ('Calculate sum: %s + %s = %s' % (x,y, my_client.service.sum(x, y)))
print ('Calculate quotient: %s / %s = %s' % (x,y, my_client.service.div(x, y)))
print ('Calculate product: %s * %s = %s' % (x,y, my_client.service.prod(x, y)))