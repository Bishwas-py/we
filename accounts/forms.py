from django import forms
from .models import School
class LoginForm(forms.Form):
    # username = forms.CharField(max_length=95, required=False)
    # password = forms.CharField(max_length=95, required=False)
    class Meta:
        model = School
        fields = ['username', 'password']