from django import forms

from .models import Lookforjob

class LookforjobForm(forms.ModelForm):

    class Meta:
        model = Lookforjob
        fields = ('title', 'text','email')