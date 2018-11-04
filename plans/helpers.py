from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PlanMixin(View):
    # to validate access to create folders based on plan

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        plan = self.request.user.plan.name
        folders = self.request.user.folder_set.count()
        if plan == 'P' and folders == 1:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
