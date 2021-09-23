from django.db import models

# Create your models here.
class Diaper(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Bottle(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class BottleNipple(models.Model):
    name = models.CharField(max_length=100)
    flow = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class DiaperComment(models.Model):
    name = models.ForeignKey(Diaper, on_delete=models.CASCADE, related_name='DiaperComments')
    newparent = models.CharField(max_length=100)
    review = models.CharField(max_length=500)

    def __str__(self):
        return self.newparent

class BottleComment(models.Model):
    name = models.ForeignKey(Bottle, on_delete=models.CASCADE, related_name='BottleComments')
    newparent = models.CharField(max_length=100)
    review = models.CharField(max_length=500)

    def __str__(self):
        return self.newparent

class BNComment(models.Model):
    name = models.ForeignKey(BottleNipple, on_delete=models.CASCADE, related_name='BNComments')
    newparent = models.CharField(max_length=100)
    review = models.CharField(max_length=500)

    def __str__(self):
        return self.newparent