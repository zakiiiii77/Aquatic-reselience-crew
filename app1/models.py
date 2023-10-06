from django.db import models

# Create your models here.
class Articles(models.Model):
    Article_name = models.CharField(max_length=100)
    Article_number = models.CharField(max_length=100)

    class Meta:
      verbose_name_plural = "app1"

    def __str__(self):
        return self.Article_name