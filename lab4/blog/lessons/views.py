from django.shortcuts import render
from django.http import Http404
from .models import Lesson


def archive(request):
    return render(request, 'archive.html', {"lessons": Lesson.objects.all()})


def get_lesson(request, lesson_id):
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        return render(request, 'lesson.html', {"lesson": lesson})
    except Lesson.DoesNotExist:
        raise Http404