from django import forms 
from .models import user

class registerUserForm(forms.ModelForm):
    password = forms.CharField(max_length=30)
    confirmPassword = forms.CharField(max_length=30)
    class Meta:
        model = user
        fields = ["first_name","last_name","username","email","phone_number"]
    
    def clean(self, *args, **kwargs):
        cleaned_data = super(registerUserForm, self).clean()

        password = cleaned_data.get("password")
        confPassword = cleaned_data.get("confirmPassword")

        if password != confPassword:
            raise forms.ValidationError("password does not match!")