from django.shortcuts import render
from django.http import HttpResponseRedirect
from vidya.models import Videogame
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'VideogameDB/index.html'
	context_object_name = 'vidya_list'
	def get_queryset(self):
		return Videogame.objects.order_by('-title')
