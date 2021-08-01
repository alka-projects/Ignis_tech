from django import forms
from Ignis_app.models import event

class eventForm(forms.ModelForm):
    class Meta:
        model=event
        # fields='__all__'
        fields=['event_name','date','time','location','image']
