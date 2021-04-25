from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Create your models here.

class School(models.Model):
    SCHOOL_TYPE = [
        ('PRIMARY', 'Primary'),
        ('MIDDLE', 'Middle'),
        ('HIGH', 'High')
    ]

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, verbose_name=_("owner"), on_delete=models.CASCADE)
    level = models.CharField(
        max_length=50,
        choices=SCHOOL_TYPE,
        default='PRIMARY'
        )
    established_on = models.DateField(_("established_on"), auto_now=False, auto_now_add=False)
    address = models.TextField(_("address"))
    country = models.ForeignKey(
        "address.Country", 
        verbose_name=_("country"), 
        on_delete=models.SET_NULL,
        null=True
    )
    city = models.ForeignKey(
        "address.City", 
        verbose_name=_("city"), 
        on_delete=models.SET_NULL,
        null=True    
    )

    state = models.ForeignKey(
        "address.State", 
        verbose_name=_("state"), 
        on_delete=models.SET_NULL,
        null=True    
    )

    updated_on = models.DateTimeField(_("updated_on"), auto_now=True, auto_now_add=False)
    created_on = models.DateTimeField(_("created_on"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    