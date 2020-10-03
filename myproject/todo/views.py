from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Todo
def sayHi(request):
    # return  HttpResponse('hi ali')
    return render(request,'jinja2.html')


def all_todo(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request, 'todos.html',context )

def detail(request , id):
    todo = Todo.objects.get(id=id)
    context = {'todo': todo}
    return render(request, 'detail.html',context )
