from rest_framework import serializers

from bus.models import Route, RouteInfo, Passenger


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'no_of_stops']


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'email', 'name', 'profile_pic']
        read_only_fields = ('id',)


class PassengerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['wallet', 'boarding_flag']


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'beacon_id', 'status']


class RouteInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteInfo
        fields = ['last_know_stop',]
