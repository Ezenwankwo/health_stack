import datetime

from django.shortcuts import render, redirect

from users.decorators import twofa_required
from .models import Plan


#class ChoosePlan(LoginRequiredMixin, TemplateView):
    #template_name = 'choose_plan.html'

@twofa_required
def choose_plan(request):
    return render(request, 'plan/choose_plan.html')


@twofa_required
def personal_plan(request):
    plan = Plan.objects.create_plan(account=request.user,
                                    name='P',
                                    created=datetime.datetime.now)
    return redirect('list_file')


@twofa_required
def family_plan(request):
    plan = Plan.objects.create_plan(account=request.user,
                                    name='F',
                                    created=datetime.datetime.now)
    return redirect('list_file')
