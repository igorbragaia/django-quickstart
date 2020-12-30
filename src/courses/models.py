from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    summary = models.TextField()

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"id": self.id})
