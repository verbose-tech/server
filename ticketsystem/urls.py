"""ticketsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from bus.views import RouteListView, BeaconListView, RouteInfoView, PassengerView, PassengerUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/bus/passenger/$', PassengerView.as_view(), name='passenger_create'),
    url(r'^api/bus/passenger/(?P<pk>\d+)/$', PassengerUpdateView.as_view(), name='passenger_update'),
    url(r'^api/bus/route/$', RouteListView.as_view(), name='bus_route_list'),
    url(r'^api/bus/beacon/$', BeaconListView.as_view(), name='bus_beacon_list'),
    url(r'^api/bus/routeinfo/(?P<pk>\d+)/$', RouteInfoView.as_view(), name='bus_route_info'),
]
