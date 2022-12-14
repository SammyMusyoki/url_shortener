from django.db import models
from .utils import create_shortened_url

# Create your models here.
class Shortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)

    class Meta:

        ordering = ["-created"]
    
    def save(self, *args, **kwargs):
        # if the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

