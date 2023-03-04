from dataclasses import fields
from tkinter import Widget
from django.core import validators
from django import forms
from .models import User


class studentregistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter your Email ID"}),
            'password': forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': "Enter your Password"}),

        }
