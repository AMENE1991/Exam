from django import forms

from AutoRu.models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["price", "brand"]
