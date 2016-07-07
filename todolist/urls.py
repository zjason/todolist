from django.conf.urls import url
from . import views

urlpatterns = [
    # /todolist/
    # r means regular expression
    # This is the defulat url for todolist
    url(r'^$', views.index, name='index'),
    # /todolist/list_id
    url(r'^(?P<list_id>[0-9]+)/$', views.detail, name='detail'),
]