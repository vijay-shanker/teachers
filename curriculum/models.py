from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
# Create your models here.

class Subject(models.Model):
    SUBJECT_TYPE = (
        (_('TH'), _('Theory')),
        (_('PR'), _('Practical'))
    )

    name = models.CharField(_("Subject"), max_length=50)
    code = models.CharField(_("code"), max_length=50)
    subject_type = models.CharField(
        _("subject_type"), 
        choices = SUBJECT_TYPE,
        max_length=50)

    def __str__(self):
        return self.name

class Grade(models.Model):
    grade = models.CharField(_("Grade"), max_length=50)
    subjects = models.ManyToManyField("curriculum.Subject", verbose_name=_("Grades"))
    class_teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=_("class_teacher"), 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.grade
