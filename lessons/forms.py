from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError('Lesson name must be at least 4 characters long.')
        return name