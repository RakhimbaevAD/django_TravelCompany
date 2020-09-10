from django.contrib import admin
from .models import Country, Hotel_type, Food_type, Beach_type, \
    Hotel, Food_in_hotel, Services, Hotel_photos, Reviews, Orders

# Register your models here.

admin.site.register(Country)
admin.site.register(Hotel_type)
admin.site.register(Food_type)
admin.site.register(Beach_type)
admin.site.register(Hotel)
admin.site.register(Food_in_hotel)
admin.site.register(Services)
admin.site.register(Hotel_photos)
admin.site.register(Reviews)
admin.site.register(Orders)
