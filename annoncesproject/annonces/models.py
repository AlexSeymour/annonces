from django.db import models
from user.models import Profile
import datetime
from django.utils.text import slugify


STATUS_CHOICES = (
    (0, "Active"),
    (1, "En attente"),
    (2, "Supprimée"),
    (3, "Désactivée")
)

class Annonce(models.Model):
    user = models.ForeignKey(Profile, related_name='annonce')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    slug_title = models.SlugField(unique=True)
    text = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ('-date',)


    def __str__(self):
        return "{} - {}".format(self.user.user.username, self.title)

    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)

        if self.slug_title == '':
            self.slug_title = "None"

        super(Annonce, self).save(*args, **kwargs)



class Image(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='images')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    is_thumb = models.BooleanField(default=False)

    def __str__(self):
        return self.image.name