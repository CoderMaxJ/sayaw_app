from django.contrib import admin
from .models import CustomUser, rooms,cottages,booking,paid,Guest_list,nationality,information,message_storage_1,message_storage_2,message_storage_3,gcash,paymaya
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(rooms)
admin.site.register(cottages)
admin.site.register(booking)
admin.site.register(paid)
admin.site.register(Guest_list)
admin.site.register(nationality)
admin.site.register(information)
admin.site.register(message_storage_1)
admin.site.register(message_storage_2)
admin.site.register(message_storage_3)
admin.site.register(gcash)
admin.site.register(paymaya)
