from django.db import models

from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# need   to fix user
class Candidate(models.Model):
    # values for db
    IN_PROGRESS_APPLICATION = 'in_progress_application'
    REJECTED_APPLICATION = 'rejected_application'
    NEW_APPLICATION = 'new_application'
    CONFIRMED_APPLICATION = 'confirmed_application'

    APPLICATION_CHOICES = (
        (IN_PROGRESS_APPLICATION, _('Application is in progress')),
        (REJECTED_APPLICATION, _('Sorry, application was rejected')),
        (NEW_APPLICATION, _('Create a new application')),
        (CONFIRMED_APPLICATION, _('Application was confirmed')),
    )
    first_name = models.CharField(_('First Name'), max_length=30, db_index=True, null=False, blank=False)
    last_name = models.CharField(_('las Name'), max_length=30, db_index=True, null=False, blank=False)
    email = models.EmailField(_('Email'), max_length=100, db_index=True, null=False, blank=False)

    birth_date = models.DateTimeField(_('birthday'), blank=True, null=True, db_index=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, db_index=True)

    phone_number = models.CharField(
        _('Phone Number'),
        max_length=8,
        validators=[MinLengthValidator(8)],
        blank=False, db_index=True, null=False)
    availability = models.FloatField(
        _('availability'),
        validators=[MinValueValidator(0.0), MaxValueValidator(0.6)],
        blank=True,
        null=True, db_index=True)
    experience_years = models.FloatField(
        _('availability'),
        validators=[MinValueValidator(0.1)],
        blank=True,
        null=True, db_index=True)
    curriculum_vitae = models.FileField(_('cv'), blank=True, default='', null=True, upload_to="candidates/",
                                        db_index=True)
    message = models.TextField(_(' state of  job application '), blank=True, null=True, db_index=True)
    application_status = models.CharField(_('Action Name'), max_length=45, choices=APPLICATION_CHOICES,
                                          default='new_application', db_index=True)

    def __str__(self):
        return self.email
