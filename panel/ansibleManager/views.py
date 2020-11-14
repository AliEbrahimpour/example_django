from django.shortcuts import render
from .models import PlayBook


def home(request):
    playbooks = PlayBook.objects.all()
    context = {'playbooks': playbooks}
    return render(request, 'home.html', context)


def detail(request, id):
    playbook = PlayBook.objects.get(id=id)
    context = {'playbook': playbook}
    return render(request, 'detail.html', context)
