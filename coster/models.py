# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tenant_schemas.models import TenantMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    created_on = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=1, default="s")

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Rides(models.Model):
    name = models.CharField(max_length=100)
    danger_rate = models.FloatField()
    danger = models.CharField(max_length=100)
    age_limit = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name