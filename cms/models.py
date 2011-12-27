from django.db import models

# Create your models here.

class Guestbook(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField(max_length=2000)

    def __unicode__(self):
        return '%s %s' % (self.title,self.content)

    class Admin():
        pass