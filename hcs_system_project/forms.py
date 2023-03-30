from django import forms
from apps.hcs_system.models import CreatingApplication


class CreatingApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].empty_label = "Выберите адрес"

    class Meta:
        model = CreatingApplication
        fields = ['address', 'subject_appeal', 'your_message', 'file']
