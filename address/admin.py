from django.contrib import admin
from address.models import City, Country, State
# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(State)