from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from captcha.fields import ReCaptchaField

# Create your forms here.
class UserCreationForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',  'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',  'class': 'form-control'}))

    captcha = ReCaptchaField(required=True)

    class Meta:
        model = User
        fields = ("username", "captcha")
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CreateTask(forms.ModelForm):
        category = forms.ModelChoiceField(queryset=models.Category.objects.all(), empty_label="Select Category",
                                      widget=forms.Select(attrs={'class': 'form-control'}))

        class Meta:
             model = models.Task
             fields = ['title','description','complete', 'category']

             widgets = {
                  'title': forms.TextInput(attrs={'placeholder': 'Title',  'class': 'form-control'}),
                  'description': forms.Textarea(attrs={'placeholder': 'Enter Description',  'class': 'form-control'}),
                  'complete': forms.CheckboxInput(attrs={'placeholder': 'Title',  'class': 'form-check-label' }),
                  'category': forms.Select(attrs={'class': 'form-control'})
             }