from django import forms
from .models import FamilyInfo


class FamilyInfoForm(forms.ModelForm):

    class Meta:
        model = FamilyInfo
        fields = '__all__'
