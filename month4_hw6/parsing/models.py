from django.db import models


class PGParser(models.Model):
    title_url = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='')
    rating = models.FloatField(null=True)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title_text
