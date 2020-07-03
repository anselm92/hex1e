from django.contrib import admin

# Register your models here.
from webapp.models import Blog, Raffle, RaffleParticipant

admin.site.register(Blog)
admin.site.register(Raffle)
admin.site.register(RaffleParticipant)