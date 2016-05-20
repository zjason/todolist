from django.shortcuts import render
from django.http import HttpResponse
from .models import List

# Create your views here.
def index(request):
    all_list = List.objects.all()
    html = '<h1>This is your to do list</h1>'

    for list in all_list:
        url = '/todolist/' + str(list.id)+'/'
        html += '<a href="' + url + '">' + list.listname + '</a><br>'

    return HttpResponse(html)

def detail(request, list_id):
    return HttpResponse("<h1>This is todolist:"+list_id+"</ht>")