from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        if self.firstname:
            return u'%s %s' % (self.firstname, self.lastname)
        else:
            return self.lastname


class Book(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateField(null=True, blank=True)
