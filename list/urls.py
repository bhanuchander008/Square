from django.conf.urls import url,include
from .rest_api import Test,getNumber,getNumber,get,post

urlpatterns = [
                url(r'^test/',Test),
                url(r'^apinum/(?P<_Number>[\w\-]+)/$',getNumber),
                url(r'^apiget/(?P<_num>[0-99]+)/',get),
                url(r'^apipost/(?P<_values>[0-99,-]+)/',post)
                url(r'^api2/',post)
]
