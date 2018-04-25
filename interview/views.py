from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', {'text' : 'Hey, Introduce yourself'})
