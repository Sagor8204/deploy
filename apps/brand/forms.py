from django.forms import ModelForm
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class BrandForm(ModelForm):
    class Meta:
        model = BrandModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "order": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "is_active": forms.NullBooleanSelect(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class BrandDetailsForm(ModelForm):
    brand = forms.ModelChoiceField(
        queryset=BrandModel.objects.all().order_by("name"),
        label="", empty_label="Select Brand",
        required=True
    )

    left_content = CKEditorWidget(config_name="awesome_ckeditor")
    right_content = CKEditorWidget(config_name="awesome_ckeditor")

    class Meta:
        model = BrandDetailsModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "efficiency_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "why_right_choice_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "efficiency_description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "why_right_choice_description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "why_right_choice": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "what_makes_different": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
