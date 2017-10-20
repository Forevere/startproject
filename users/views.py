# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import  logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

@csrf_protect
def register(requset):
    if requset.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=requset.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=requset.POST['password1'])
            login(requset, authenticated_user)
            return  HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return  render(requset, 'users/register.html', context)


