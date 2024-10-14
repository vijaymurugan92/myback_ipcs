from django import forms
from .models import vvapp


class vvappForm(forms.ModelForm):
    class Meta:
        model = vvapp
        fields = "__all__"