from django.shortcuts import render
from .models import Lesson


def archive(request):
    return render(request, 'archive.html', {"lessons": Lesson.objects.all()})