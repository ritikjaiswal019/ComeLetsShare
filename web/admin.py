from django.contrib import admin
from .models import SubscribedMail, UserQuery, PastEvent, UpcomingEvent

# Register your models here.
admin.site.register(SubscribedMail)
admin.site.register(UserQuery)
admin.site.register(UpcomingEvent )
admin.site.register(PastEvent)
