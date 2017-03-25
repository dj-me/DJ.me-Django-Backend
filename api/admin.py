from django.contrib import admin

# Register your models here.

from api.models import user , hostsong , djsessions , finalplaylist 


admin.site.register(user)
admin.site.register(hostsong)
admin.site.register(djsessions)
admin.site.register(finalplaylist)
