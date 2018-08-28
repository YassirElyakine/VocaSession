from django.db import models

class Vocabulary(models.Model):
    title = models.CharField(max_length=100)
    meaning = models.CharField(max_length=1000)
    def __str__(self):
        return self.title