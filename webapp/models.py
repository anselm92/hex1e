from django.db import models

# Create your models here.
from webapp.fileupload import fs, blog_file_upload_handler, raffle_file_upload_handler


class Raffle(models.Model):
    title = models.CharField(max_length=100, default=None, blank=True)
    # HTML Field
    description = models.CharField(max_length=1000, default=None, blank=True)
    image = models.FileField(storage=fs, upload_to=raffle_file_upload_handler, blank=True, null=True)
    image_legacy = models.FileField(storage=fs, upload_to=raffle_file_upload_handler, blank=True, null=True)
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
    image_legacy = models.FileField(storage=fs, upload_to=blog_file_upload_handler, blank=True, null=True)
    date_posted = models.DateTimeField(auto_created=True, auto_now=True, editable=True, )

    class Meta:
        ordering = ['-date_posted']


class BuildImage(models.Model):
    image = models.FileField(storage=fs, upload_to=blog_file_upload_handler)
    title = models.CharField(max_length=100, default=None, blank=True)

    def __unicode__(self):
        return self.image.name

    def __str__(self):
        return self.image.name

class Build(models.Model):
    title = models.CharField(max_length=100, default=None, blank=True)
    content = models.CharField(max_length=2000, default="", blank=True, null=True)
    specs = models.CharField(max_length=2000, default="", blank=True, null=True)
    date_posted = models.DateTimeField(auto_created=True, auto_now=True, editable=True, )
    order = models.IntegerField(blank=True, null=True)
    last_order = models.IntegerField(blank=True, null=True, editable=False)
    link = models.CharField(max_length=100, default=None, blank=True, null=True)
    images = models.ManyToManyField(BuildImage)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.order is None:
            if Build.objects.all().count() > 0:
                self.order = Build.objects.all().order_by('order').last().order + 1
            else:
                self.order = 0
            self.last_order = self.order
            result = super(Build, self).save(force_insert, force_update, using, update_fields)
        if self.order != self.last_order:
            self.last_order = self.order
            result = super(Build, self).save(force_insert, force_update, using, update_fields)
            next_build = Build.objects.filter(order__gte=self.order)
            if next_build.filter(order=self.order).exists() and next_build.exclude(id=self.id).exists():
                next_build = next_build.exclude(id=self.id).order_by('order').first()
                next_build.order = self.order + 1
                next_build.save()
            # re-sort
        else :
            result = super(Build, self).save(force_insert, force_update, using, update_fields)
        return result

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title + f" ({self.order})"

    def __str__(self):
        return self.title + f" ({self.order})"