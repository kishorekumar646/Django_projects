from django import forms
from polls.models import Registration

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
      