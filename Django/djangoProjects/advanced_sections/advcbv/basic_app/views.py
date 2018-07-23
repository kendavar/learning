from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models


class IndexView(TemplateView):
    template_name="index.html"

class SchoolListView(ListView):
    model =models.School

class SchoolDetailView(DetailView):
    model =models.School
    context_object_name ='school_details'
    template_name = 'basic_app/school_details.html'
