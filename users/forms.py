from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control',})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', })
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', })
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', })
        self.fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 8 символов.'

class UserUpdateform(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateform, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', })
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', })



class ProfileUpdateform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateform, self).__init__(*args, **kwargs)
        self.fields['img'].required = False
        self.fields['b_data'].widget = forms.DateInput(attrs={'class': 'form-control', })
        self.fields['height'].widget = forms.NumberInput(attrs={'class': 'form-control', })
        self.fields['weight'].widget = forms.NumberInput(attrs={'class': 'form-control', })

    class Meta:
        model = Profile
        fields = ['b_data','height','weight','img']

