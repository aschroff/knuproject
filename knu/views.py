from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Value
from plotly.offline import plot
import plotly.graph_objects as go


def home(request):
    value_list = Value.objects.order_by('-source')[:5]
    context = {
        'value_list': value_list,
    }
    return render(request, 'knu/home.html', context)


def value(request, value_id):
    valueobject = get_object_or_404(Value, pk=value_id)
    context = {
        'value': valueobject,
    }
    return render(request, 'knu/detail.html', {'value': valueobject})

def index(request):
    value_list = Value.objects.order_by('-source')
    context = {
        'value_list': value_list,
    }
    return render(request, 'knu/index.html', context)

def location(request):
    value_list = Value.objects.order_by('-source')[:5]
    context = {
        'value_list': value_list,
    }
    return render(request, 'knu/location.html', context)

