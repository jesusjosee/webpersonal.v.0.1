from django.shortcuts import get_object_or_404, render
from .models import Project

# Create your views here.


def portfolio(request):
    proyectos = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'proyectos': proyectos})