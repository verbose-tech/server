from django.contrib import admin

from bus.models import Route, Beacon, RouteInfo, Passenger


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    pass


@admin.register(Beacon)
class BeaconAdmin(admin.ModelAdmin):
    pass


@admin.register(RouteInfo)
class RouteInfoAdmin(admin.ModelAdmin):
    pass
