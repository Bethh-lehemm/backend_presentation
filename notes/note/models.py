from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(unique=True, max_length=300)
    contents = models.TextField(unique=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title