# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Photo(models.Model):
    name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)

    def __unicode__(self):
        return self.name + ' ' + self.last_name
    def full_name(self):
        return self.name + ' ' + self.last_name