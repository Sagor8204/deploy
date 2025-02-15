from django.forms import ModelForm
from django import forms
from .models import *
from apps.brand.models import BrandModel

class ProductForm(ModelForm):
    brand = forms.ModelChoiceField(
        queryset=BrandModel.objects.all().order_by("name"),
        label="", empty_label="Select Brand",
        required=True
    )

    viscosity = forms.ModelChoiceField(
        queryset=ViscosityModel.objects.all().order_by("title"),
        label="", empty_label="Select Viscosity",
        required=False
    )

    applications = forms.ModelChoiceField(
        queryset=ApplicationsModel.objects.all().order_by("title"),
        label="", empty_label="Select Application",
        required=False
    )

    oil_type = forms.ModelChoiceField(
        queryset=OilTypeModel.objects.all().order_by("title"),
        label="", empty_label="Select Oil Type",
        required=False
    )

    product_range = forms.ModelChoiceField(
        queryset=ProductRangeModel.objects.all().order_by("title"),
        label="", empty_label="Select Product Range",
        required=False
    )

    sectors = forms.ModelChoiceField(
        queryset=SectorsModel.objects.all().order_by("title"),
        label="", empty_label="Select Sectors",
        required=False
    )

    class Meta:
        model = ProductModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "short_description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "industry_specifications": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "FG_code": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "OEM_approvals": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "OEM_performance": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class OilTypeForm(ModelForm):
    class Meta:
        model = OilTypeModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ProductRangeForm(ModelForm):
    class Meta:
        model = ProductRangeModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ViscosityForm(ModelForm):
    class Meta:
        model = ViscosityModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ApplicationsForm(ModelForm):
    class Meta:
        model = ApplicationsModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class SectorsForm(ModelForm):
    class Meta:
        model = SectorsModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class LubricantCategoryForm(ModelForm):
    class Meta:
        model = LubricantCategoryModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "category": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class LubricantCategoryYearForm(ModelForm):
    category = forms.ModelChoiceField(
        queryset=LubricantCategoryModel.objects.all().order_by("category"),
        label="", empty_label="Select Category",
        required=True
    )

    class Meta:
        model = LubricantCategoryYearModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "year": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class LubricantEngineCapacityForm(ModelForm):
    year = forms.ModelChoiceField(
        queryset=LubricantCategoryYearModel.objects.all().order_by("year"),
        label="", empty_label="Select Year",
        required=True
    )

    class Meta:
        model = LubricantEngineCapacityModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "engine_capacity": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class LubricantSpecificationForm(ModelForm):
    engine_capacity = forms.ModelChoiceField(
        queryset=LubricantEngineCapacityModel.objects.all().order_by("engine_capacity"),
        label="", empty_label="Select Engine Capacity",
        required=True
    )

    class Meta:
        model = LubricantSpecificationModel
        exclude = ('created_at', 'updated_at')

        widgets = {
            "model_name": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "fuel_type": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "power": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "production_year": forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


