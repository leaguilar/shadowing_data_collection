from django.forms import ModelForm, RadioSelect
from .models import ObservationModel


class ObservationForm(ModelForm):
    class Meta:
        model = ObservationModel
        fields = '__all__'
        widgets = {
            'zone': RadioSelect,
            'interaction_type': RadioSelect
        }
