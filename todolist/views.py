from django.shortcuts import render
from django.http import HttpResponse
from .models import List,Task
from django.template import loader

# Create your views here.
def index(request):
    all_list = List.objects.all()
    template = loader.get_template('todolist/index.html')
    context = {
        'all_list': all_list,
    }

    return HttpResponse(template.render(context,request))

def detail(request, list_id):
    html = '<h1>Task in list: '+list_id+'<h1>'
    all_task = Task.objects.all()
    for task in all_task:
        html += 'task id: ' + str(task.id) + ' task name: ' + task.task_desc
    return HttpResponse(html)