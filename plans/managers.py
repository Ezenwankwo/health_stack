from django.db import models


class PlanManager(models.Manager):
    
    def create_plan(self, account, name, created):
        plan = self.model(account=account, name=name, created=created)
        plan.save()
        return plan
