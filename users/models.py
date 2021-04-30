from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE
    )
    dob = models.DateField(_("date_of_birth"), auto_now=False, auto_now_add=False)
    grade = models.CharField(_("class"), max_length=50)
    section = models.CharField(_("section"), max_length=50)
    roll_no = models.CharField(_("roll_no"), max_length=50)
    admission_no = models.UUIDField(_("admission_no"), editable=False)

    def __str__(self):
        return self.user.firstname + ' ' +self.user.lastname


class Teachers(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        "curriculum.Subject", 
        verbose_name=_("subject"), 
        on_delete=models.CASCADE
    )
    highest_qualification = models.CharField(_("highest_qualification"), max_length=50)
    dob = models.DateField(_("date_of_birth"), auto_now=False, auto_now_add=False)
    employee_code = models.CharField(_("employee_code"), max_length=50)
    employee_grade = models.CharField(_("employee_grade"), max_length=50)
    salary = models.FloatField(_("salary"))

    def __str__(self):
        return self.user.firstname + ' ' +self.user.lastname
