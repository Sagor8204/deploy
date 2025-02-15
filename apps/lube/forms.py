from django.forms import ModelForm
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class NewsAndEventsForm(ModelForm):
    class Meta:
        model = NewsAndEventsModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "date": forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }
