from django.db import models
from django.conf import settings

from .managers import PlanManager


class Plan(models.Model):
    PERSONAL = "P"
    FAMILY = "F"
    NAME = (
        (PERSONAL, 'Personal'),
        (FAMILY, 'Family'),
    )
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=1, choices=NAME, default=PERSONAL)
    created = models.DateTimeField(auto_now_add=True)
    objects = PlanManager()

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"
        ordering = ("-created",)

    def __str__(self):
        return '{0} - {1}'.format(self.account, self.name)
