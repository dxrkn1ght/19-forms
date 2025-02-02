from django.shortcuts import render, redirect, get_object_or_404
from .models import Test
from .forms import TestForm
from django.forms import inlineformset_factory
from questions.models import Question
from questions.forms import QuestionForm


def home(request):
    return render(request, 'index.html')

def test_list(request):
    tests = Test.objects.all()
    ctx = {'tests':tests}
    return render(request, 'tests/test-list.html', ctx)

def create_test(request):
    QuestionFormSet = inlineformset_factory(Test, Question, form=QuestionForm, extra=2)
    if request.method == 'POST':
        form = TestForm(request.POST)
        formset = QuestionFormSet(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            formset = QuestionFormSet(request.POST, instance=test)
            if formset.is_valid():
                test.save()
                formset.save()
                return redirect('tests:list')
    else:
        form = TestForm()
        formset = QuestionFormSet()

    ctx = {'form':form, 'formset':formset}
    return render(request, 'tests/test-formset.html', ctx)

def delete_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('tests:list')

def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()
    ctx = {'test':test, 'questions':questions}
    return render(request,'tests/detail.html', ctx)

def edit_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    QuestionFormSet = inlineformset_factory(Test, Question, form=QuestionForm, extra=1)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        formset = QuestionFormSet(request.POST, instance=test)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('tests:list')
    else:
        form = TestForm(instance=test)
        formset = QuestionFormSet(instance=test)
    ctx = {
        'form':form,
        'formset':formset,
        'test':test
    }
    return render(request, 'tests/test-formset.html', ctx)