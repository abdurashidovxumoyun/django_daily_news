from django.db import models
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField(upload_to='media/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Agar slug bo'sh bo'lsa
            self.slug = slugify(self.title)  # slugify funksiyasidan foydalanish
        super().save(*args, **kwargs)