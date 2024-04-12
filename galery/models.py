from django.db import models
from datetime import datetime

class Photo(models.Model):

    CATEGORIES = [
        ("NEBULA", "Nebula"),
        ("STAR", "Star"),
        ("GALAXY", "Galaxy"),
        ("planet", "Planet"),
    ]

    name: str = models.CharField(max_length=100, null=False, blank=False)
    subtitle: str = models.CharField(max_length=150, null=False, blank=False)
    description: str = models.TextField(null=False, blank=False)
    photoPath: str = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    category: str = models.CharField(max_length=50, choices=CATEGORIES, default='')
    date: datetime = models.DateTimeField(default=datetime.now, blank=False)
    publish: bool = models.BooleanField(default=False)

    def __str__(self):
        return self.name