from django.shortcuts import render, redirect
from .forms import QuestionForm


def create_question(request):
    form = QuestionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tests:list')

    return render(request, 'tests/test-formset.html', {'form': form})
