from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson
from .forms import LessonForm


def lessons_list(request):
    return render(request, 'lessons/lesson-list.html', {'lessons': Lesson.objects.all()})


def create_lesson(request):
    form = LessonForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lessons:list')

    return render(request, 'lessons/lesson-create.html', {'form': form})


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessons/lesson-detail.html', {'lesson': lesson, 'tests': lesson.tests.all()})


def delete_lesson(request, pk):
    get_object_or_404(Lesson, pk=pk).delete()
    return redirect('lessons:list')


def edit_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    form = LessonForm(request.POST or None, instance=lesson)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lessons:list')

    return render(request, 'lessons/lesson-create.html', {'form': form, 'lesson': lesson})
