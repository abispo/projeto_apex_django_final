from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def dashboard(request):
    return render(request, 'users/dashboard.html')


def user_update(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return HttpResponseRedirect(reverse('users:success'))

    elif request.method == 'GET':
        return HttpResponseRedirect(reverse('users:dashboard'))

def success(request):
    return render(request, 'users/success.html')
