from django import forms
from .models import Number






class sendForm(forms.ModelForm):
     class Meta:
          model = Number
          fields = ('phone_number', )




