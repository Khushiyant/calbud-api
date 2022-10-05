from django.contrib import admin
from .models import UserAccount, PremiumUserAccount

# Register your models here.

admin.register(UserAccount)
admin.register(PremiumUserAccount)