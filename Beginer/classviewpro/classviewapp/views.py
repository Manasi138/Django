from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Food
# Create your views here.
#to create, update, delete
# import (dja) 
#to insert into database need CreateView

class AddFood(CreateView):
    model=Food
    fields=['foodName','foodType','foodCategory','foodPrice']
    success_url="/success/"
    
class TemplateDemo(TemplateView):
    template_name="classviewapp/Success.html"
    
class FoodRecords(ListView):
    model=Food
    template_name="classviewapp/FoodList.html"
    context_object_name="foods"
    
class FoodDetails(DetailView):
    model=Food
    template_name="classviewapp/FoodDetails.html"
    context_object_name="food"