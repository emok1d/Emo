from django.db import models
from django.db.models.signals import post_save
from taggit.managers import TaggableManager


class Event(models.Model):
    name = models.CharField((""), max_length=128)
    date = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    #tickets = 
    description = models.TextField((""))
    genre = TaggableManager()
    age_category = [
        ("0+", "0+"),
        ("6+", "6+"),
        ("12+", "12+"),
        ("16+", "16+"),
        ("18+", "18+"),
    ]
    ages = models.CharField(max_length=3, choices=age_category, default="0+")
    image = models.ImageField((""), upload_to="apps/events/static/img", height_field=None, width_field=None, max_length=None)
    slug = models.CharField(verbose_name='url мероприятия', max_length=255, blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('events:', kwargs={'slug': self.slug}) 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)
