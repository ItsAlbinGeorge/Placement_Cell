from django.contrib import admin

# Register your models here.
from .models import Candidate,OTP,Placements,Volunteer

admin.site.register(Candidate)
admin.site.register(OTP)
admin.site.register(Placements)
admin.site.register(Volunteer)