from django.contrib import admin

# Register your models here.

from users.models import Users


# Register your models here.
from users.models import CustomUser


admin.site.register(CustomUser)
admin.site.register(Users)