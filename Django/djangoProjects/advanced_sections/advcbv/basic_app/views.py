from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)



class IndexView(TemplateView):
    template_name="index.html"

class SchoolListView(ListView):
    model =models.School

class SchoolDetailView(DetailView):
    model =models.School
    context_object_name ='school_details'
    template_name = 'basic_app/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model=models.School
