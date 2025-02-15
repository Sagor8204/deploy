from django.forms import ModelForm
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from apps.brand.models import BrandModel

class OurExpertsForm(ModelForm):
    class Meta:
        model = OurExpertsModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "designation": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class AboutForm(ModelForm):
    content = CKEditorWidget(config_name="awesome_ckeditor")
    director_description = CKEditorWidget(config_name="awesome_ckeditor")
    
    class Meta:
        model = AboutModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "hero_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "director_name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "director_designation": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "mission": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "vision": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class AboutSliderForm(ModelForm):
    class Meta:
        model = AboutSliderModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "sub_title": forms.TextInput(
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


class ContactDetailForm(ModelForm):
    class Meta:
        model = ContactDetailModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "phone_number": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "address": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class GetInTouchForm(ModelForm):
    class Meta:
        model = GetInTouchModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "last_name": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "phone_number": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "email": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "cover_letter": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class QueryForm(ModelForm):
    class Meta:
        model = QueryModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "phone_number": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "brand": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "product": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

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

class HomeModelForm(ModelForm):
    class Meta:
        model = HomeModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "hero_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "find_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "find_description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "distribution_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "distribution_description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class CompanyModelForm(ModelForm):
    class Meta:
        model = CompanyModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "lubricant_distributions": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "districts_covered": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "types_of_products": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "annual_production": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "dealers_of_bangladesh": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class BusinessSolutionsForm(ModelForm):
    brand = forms.ModelChoiceField(
        queryset=BrandModel.objects.all().order_by("name"),
        label="", empty_label="Select Brand",
        required=True
    )

    class Meta:
        model = BusinessSolutionsModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class AgricultureLubricantsForm(ModelForm):
    class Meta:
        model = AgricultureLubricantsModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "hero_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "diagnostics": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "fluid_i": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "academy": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "distribute_title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "distribute_description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class AgricultureLubricantsSliderForm(ModelForm):
    class Meta:
        model = AgricultureLubricantsSliderModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "sub_title": forms.TextInput(
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


class DistributionDivisionForm(ModelForm):
    class Meta:
        model = DistributionDivisionModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "division": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class DistributionDistrictForm(ModelForm):
    division = forms.ModelChoiceField(
        queryset=DistributionDivisionModel.objects.all().order_by('division'),
        label="", empty_label="Select Division",
        required=True
    )

    class Meta:
        model = DistributionDistrictModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "district": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class DistributionPointForm(ModelForm):
    district = forms.ModelChoiceField(
        queryset=DistributionDistrictModel.objects.all().order_by('district'),
        label="", empty_label="Select District",
        required=True
    )

    class Meta:
        model = DistributionPointModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "dealer_name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "dealer_number": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class DocumentForm(ModelForm):
    class Meta:
        model = DocumentModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


