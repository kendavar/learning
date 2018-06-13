from django import forms
from AppTwo.models import user

class NewUser(forms.ModelForm):
    class Meta():
        model = user
        fields = '__all__'
