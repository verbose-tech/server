from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response

from bus.models import Route, Beacon, Passenger
from bus.serializers import RouteSerializer, BeaconSerializer, RouteInfoUpdateSerializer, PassengerSerializer, \
    PassengerUpdateSerializer


class RouteListView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class BeaconListView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = BeaconSerializer
    queryset = Beacon.objects.all()


class RouteInfoView(UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = RouteInfoUpdateSerializer
    queryset = Beacon.objects.all()

class PassengerView(CreateAPIView):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()


class PassengerUpdateView(UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = PassengerUpdateSerializer
    queryset = Passenger.objects.all()
