from django import forms
from .models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'lesson']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'lesson': forms.Select(attrs={'class': 'w-full border border-gray-300 rounded p-2'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 5:
            raise forms.ValidationError('Test name must be at least 5 characters long.')
        return name
