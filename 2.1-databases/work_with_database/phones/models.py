from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=300)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)