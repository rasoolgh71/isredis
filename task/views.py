#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import redis

# Create your views here.
def home(request):  # load page home
    return render(request,'task/home.html')
#*************************************************************
def is_redis(request):
    sel="1"
    gt="1"
    ip1 = '192.168.1.1'
    ip2 = '192.168.1.2'
    ip3 = '192.168.1.3'
    ip4 = '192.168.1.4'
    if request.method == 'POST':
        r = redis.StrictRedis()
        sel= request.POST.get('sel','')
        #if(sel)
        #listip=['192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.4']


        #return HttpResponse(sel)
        #return HttpResponse(sel)
        #r.setex('sel',sel)
        r.set('sel', sel)
        gt=r.get('sel')
        #return HttpResponse(gt)
    return render(request,'task/redis.html',context={'sel':sel,'ip1':ip1,'ip2':ip2,'ip3':ip3,'ip4':ip4,'gt':gt})


