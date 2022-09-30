from django.db import models

# Create your models here.


class Base(models.Model):
    post_id = models.IntegerField(primary_key=True, unique=True)
    by = models.CharField(max_length=50)
    score = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=500,null=True, blank=True)
    post_type = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True, max_length=2000)
    # descendants = models.IntegerField()
    kids = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.post_type})'

class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True, unique=True)
    parent = models.IntegerField()
    by = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    comment_type = models.CharField(max_length=50)

    def __str__(self):
        return (self.text)
