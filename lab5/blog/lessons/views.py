from django.shortcuts import render, redirect
from django.http import Http404
from .models import Lesson, Teacher, Group, Subject, LessonType


def archive(request):
    return render(request, 'archive.html', {"lessons": Lesson.objects.all()})


def get_lesson(request, lesson_id):
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        return render(request, 'lesson.html', {"lesson": lesson})
    except Lesson.DoesNotExist:
        raise Http404
        
def create_lesson(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == "POST":
        form = {
            'teacher': request.POST.get('teacher', ''),
            'group': request.POST.get('group', ''),
            'subject': request.POST.get('subject', ''),
            'lesson_type': request.POST.get('lesson_type', ''),
            'hours': request.POST.get('hours', ''),
            'rate_per_hour': request.POST.get('rate_per_hour', ''),
        }

        if not all(form.values()):
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_lesson.html', {
                'form': form,
                'teachers': Teacher.objects.all(),
                'groups': Group.objects.all(),
                'subjects': Subject.objects.all(),
                'lesson_types': LessonType.objects.all(),
            })

        if Lesson.objects.filter(
            teacher_id=form['teacher'],
            group_id=form['group'],
            subject_id=form['subject'],
            lesson_type_id=form['lesson_type'],
        ).exists():
            form['errors'] = "Такое занятие уже существует"
            return render(request, 'create_lesson.html', {
                'form': form,
                'teachers': Teacher.objects.all(),
                'groups': Group.objects.all(),
                'subjects': Subject.objects.all(),
                'lesson_types': LessonType.objects.all(),
            })

        lesson = Lesson.objects.create(
            teacher_id=form['teacher'],
            group_id=form['group'],
            subject_id=form['subject'],
            lesson_type_id=form['lesson_type'],
            hours=int(form['hours']),
            rate_per_hour=form['rate_per_hour'],
        )
        return redirect('get_lesson', lesson_id=lesson.id)

    return render(request, 'create_lesson.html', {
        'teachers': Teacher.objects.all(),
        'groups': Group.objects.all(),
        'subjects': Subject.objects.all(),
        'lesson_types': LessonType.objects.all(),
    })