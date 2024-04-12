from django.db import models

class Photo(models.Model):
    name: str = models.CharField(max_length=100, null=False, blank=False)
    subtitle: str = models.CharField(max_length=150, null=False, blank=False)
    description: str = models.TextField(null=False, blank=False)
    photoPath: str = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Photo [name={self.name}]"