from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    """
    Provides self-updating `created` and `modified` fields.
    """

    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        abstract = True
        ordering = (
            "-created",
            "-modified",
        )


class TimeframeMixin(models.Model):
    """
    Provides `start` and `end` fields to record a timeframe.
    """

    start = models.DateTimeField(_("start"), null=True, blank=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)

    class Meta:
        abstract = True
