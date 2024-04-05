from django.contrib import admin
from user.models import User, Organization
# Register your models here.
admin.site.register(User)
admin.site.register(Organization)