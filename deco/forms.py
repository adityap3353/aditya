from django import forms
from .models import FamilyInfo


class Aform(forms.ModelForm):
    class Meta:
        model = FamilyInfo
        fields = '__all__'
