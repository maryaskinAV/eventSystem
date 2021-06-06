from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    """ Events model """

    name = models.CharField(_("Name event"), max_length=254)
    description = models.TextField(_("Description event"), max_length=2048)

    # dates
    created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("Updated date"), auto_now=True)
    start_date = models.DateTimeField(_("Start event date"))
    end_date = models.DateTimeField(_("End event date"))

    # booleans
    draft = models.BooleanField(_("Is draft"), default=True)

    # fk
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def is_draft(self):
        return bool(self.draft)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
