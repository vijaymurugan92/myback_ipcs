from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from .models import Lmodel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


# Create your views here.
def index(request):
    return HttpResponse("hi hello iam vijay")

def My_view(request):
    if request.method == "GET":
        return HttpResponse('result')

class Myview (View):
    def get (self,request):
        return HttpResponse('result2')


class create(CreateView):
    model = Lmodel
    fields = ['title', 'description']
    template_name = 'powerapp/createmodelmodel_form.html'
    context_object_name ='data'
    success_url = "/"

class lmodellistview(ListView):
    model = Lmodel
    template_name = 'powerapp/listmodel_list.html'
    context_object_name = 'data'

class DetailView(DetailView):
    model = Lmodel
    template_name = 'powerapp/detailmodel_model.html'
    context_object_name = 'data'

class UpdateView(UpdateView):
    model = Lmodel
    fields = [
        "title",
        "description"
    ]
    template_name = 'powerapp/updatemodel_form.html'
    context_object_name = 'data'
    success_url = "/"

class DeleteView(DeleteView):
    model = Lmodel
    success_url = "/"
    template_name = 'powerapp/deletemodel_form.html'

