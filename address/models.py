from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Country(models.Model):
    name = models.CharField(_("country_name"), max_length=50)
    code = models.CharField(_("country_code"), max_length=50)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(_("state_name"), max_length=50)
    code = models.CharField(_("state_code"), max_length=50)

    class Meta:
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(_("city_name"), max_length=50)
    code = models.CharField(_("city_code"), max_length=50)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
