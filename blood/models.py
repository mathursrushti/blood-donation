from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse


class Donor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
    	return self.first_name + ' ' + self.last_name


    def get_absolute_url(self):
        return reverse('donor_detail', args=[str(self.id)])