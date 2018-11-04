from authy.api import AuthyApiClient
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm, TokenVerificationForm
from .models import Account


authy_api = AuthyApiClient(settings.ACCOUNT_SECURITY_API_KEY)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            authy_user = authy_api.users.create(
                form.cleaned_data['email'],
                form.cleaned_data['phone_number'],
                form.cleaned_data['country_code'],
            )
            if authy_user.ok():
                account_user = Account.objects.create_user(
                    form.cleaned_data['email'],
                    authy_user.id,
                    form.cleaned_data['password1']
                )
                login(request, account_user)
                return redirect('2fa')
            else:
                print(authy_user.errors())
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


#@login_required
def twofa(request):
    if request.method == 'POST':
        form = TokenVerificationForm(request.POST)
        if form.is_valid(request.user.authy_id):
            request.session['authy'] = True
            return redirect('choose_plan')
    else:
        form = TokenVerificationForm()
    return render(request, 'registration/2fa.html', {'form': form})


@login_required
def token_sms(request):
    sms = authy_api.users.request_sms(request.user.authy_id, {'force': True})
    if sms.ok():
        return JsonResponse({'sent': 'SMS request successful'})
    else:
        return JsonResponse({'not_sent': 'SMS request failed'})


@login_required
def token_voice(request):
    call = authy_api.users.request_call(request.user.authy_id, {'force': True})
    if call.ok():
        return JsonResponse({'sent':'Call request successfull'})
    else:
        return JsonResponse({'not_sent': 'Call request failed'})
