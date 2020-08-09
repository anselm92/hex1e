from django.db import models


# Create your models here.
from webapp.fileupload import fs, blog_file_upload_handler, raffle_file_upload_handler


class Raffle(models.Model):
    title = models.CharField(max_length=100, default=None, blank=True)
    # HTML Field
    description = models.CharField(max_length=1000, default=None, blank=True)
    image = models.FileField(storage=fs, upload_to=raffle_file_upload_handler, blank=True, null=True)
    active = models.BooleanField(default=True)


class RaffleParticipant(models.Model):
    raffle = models.ForeignKey(Raffle, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=50)
    participant_email = models.EmailField()

    class Meta:
        unique_together = ('participant_email', 'raffle',)


class Blog(models.Model):
    title = models.CharField(max_length=100, default=None, blank=True)
    content = models.CharField(max_length=2000, default="", blank=True, null=True)
    featured = models.BooleanField(default=False, blank=True)
    image = models.FileField(storage=fs, upload_to=blog_file_upload_handler)
    date_posted = models.DateTimeField(auto_created=True, auto_now=True, editable=True, )

    class Meta:
        ordering = ['-date_posted']
