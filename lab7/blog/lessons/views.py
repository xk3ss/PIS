from django.shortcuts import render, redirect
from django.http import Http404
from .models import Lesson, Teacher, Group, Subject, LessonType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



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
    
def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', '').strip(),
            'email':    request.POST.get('email', '').strip(),
            'password': request.POST.get('password', '').strip(),
        }
        if not form['username'] or not form['email'] or not form['password']:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
        if User.objects.filter(username=form['username']).exists():
            form['errors'] = "Пользователь с таким именем уже есть"
            return render(request, 'register.html', {'form': form})
        User.objects.create_user(
            username=form['username'],
            email=form['email'],
            password=form['password'],
        )
        return redirect('login')
    return render(request, 'register.html', {})


def login_view(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', '').strip(),
            'password': request.POST.get('password', '').strip(),
        }
        if not form['username'] or not form['password']:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
        user = authenticate(request, username=form['username'], password=form['password'])
        if user is not None:
            login(request, user)
            return redirect('archive')
        form['errors'] = "Неверный логин или пароль"
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('archive')