from django import forms
from .models import Review,RATE_CHOICES

class RateForm(forms.ModelForm):
    text = forms.CharField(max_length=400)
    score = forms.ChoiceField(choices=RATE_CHOICES)

    class Meta:
        model=Review
        fields= ['text','rating']