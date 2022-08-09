from django.forms import ModelForm, RadioSelect, DateTimeInput
from .models import ObservationModel


class ObservationForm(ModelForm):
    class Meta:
        model = ObservationModel
        fields = '__all__'
        widgets = {
            'zone': RadioSelect,
            'interaction_type': RadioSelect,
            'observation_start': DateTimeInput(attrs={'type': 'datetime-local', 'step': '1'})
        }
