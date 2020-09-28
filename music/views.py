from django.shortcuts import render
from django.views.generic import ListView,\
    DetailView
# Create your views here.
from .models import Music
from django.views.generic.edit import UpdateView, \
    DeleteView, CreateView
from django.urls import  reverse_lazy



class MusicView(ListView):
    model = Music
    template_name = 'music_list.html'

class MusicDetailView(DeleteView):
    model = Music
    template_name = 'music_detail.html'

class MusicUpdateView(UpdateView):
    model = Music
    fields = ('name','desc',)
    template_name = 'music_edit.html'

class MusicDeleteView(DeleteView):
    model = Music
    template_name = 'music_delete.html'
    success_url = reverse_lazy('music_list')



class MusicCreateView(CreateView):
    model = Music
    template_name = 'music_new.html'
    fields = ('name','image','audio','desc','date')

