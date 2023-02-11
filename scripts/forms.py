from django import forms
from .models import data
class DataSend(forms.ModelForm):
    class Meta:
        model = data
        fields = ('number','number2','password', 'nationalId' , )