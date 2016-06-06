from django.db import models
from django.utils import timezone

# Create your models here.


class Lookforjob(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=300)


    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def __str__(self):
        return  self.title