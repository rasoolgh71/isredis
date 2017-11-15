from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'index$', views.IndexView.as_view(), name='index'),
    #url(r'test$', views.Testview, name='test'),
    url(r'redis$', views.is_redis, name='redis'),
    url(r'$', views.home, name='home'),

]