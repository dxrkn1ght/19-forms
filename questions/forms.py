from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answer_1', 'correct_1', 'answer_2', 'correct_2']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'answer_1': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'answer_2': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'})
        }