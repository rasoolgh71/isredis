#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
import redis

# Create your views here.
def home(request):  # load page home
    return render(request,'task/home.html')
#*************************************************************
def is_redis(request):
    if request.method == 'POST':
        r = redis.StrictRedis()
        sel=request.POST.get('select','')
        #return HttpResponse(sel)
        #r.setex('sel',sel)
        r.set('sel', sel)

    return render(request,'task/redis.html',context={})
