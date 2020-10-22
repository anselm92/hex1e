from django.contrib import admin

# Register your models here.
from webapp.models import Blog, Raffle, RaffleParticipant, Build, BuildImage

admin.site.register(Blog)
admin.site.register(Raffle)
admin.site.register(RaffleParticipant)
admin.site.register(Build)
admin.site.register(BuildImage)