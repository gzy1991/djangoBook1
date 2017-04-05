from django.shortcuts import render

# Create your views here.
import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response




def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html',context)

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)

#Bootstrap 测试
def test(request):
     return render(request, 'test.html')



