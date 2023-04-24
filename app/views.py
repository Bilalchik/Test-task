from django.shortcuts import render
from .models import Menu


def index(request):
    objects_list = Menu.objects.filter(parent_title__isnull=True)
    return render(request, template_name='app/index.html', context={'objects_list': objects_list})


