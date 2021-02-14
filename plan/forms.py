from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import GoalForDays



class GoalForm(forms.ModelForm):

    def __init__(self, *args, **kwards):
        super(GoalForm, self).__init__(*args, **kwards)
        # Переопределяем названия полей
        self.fields['text'].label = ""
        self.fields['text'].widget = forms.TextInput(attrs={'class': 'form-control', })

    class Meta:
        model = GoalForDays
        fields = ['text']