from django import forms
from .models import vendor
from accounts.validators import allow_extension_validatotr
class registerVendorForm(forms.ModelForm):
    vendor_licence = forms.FileField(validators=[allow_extension_validatotr])
    class Meta:
        model = vendor
        fields = ["vendor_name", "vendor_licence"]