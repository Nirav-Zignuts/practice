from django.db import models
from .utils import genrate_slug
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    slug = models.SlugField(unique=True , null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = genrate_slug(self.name)
        super(Student, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    