from django.db import models
from django.db.models import Q


# user-codestore pass - code1234


class CodeModels(models.Model):
    title = models.CharField(max_length=25)
    language = models.CharField(max_length=25)
    codes = models.TextField()
    description = models.TextField()
    types = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['language']),
            models.Index(fields=['types']),
        ]

    def __str__(self):
        return self.title
