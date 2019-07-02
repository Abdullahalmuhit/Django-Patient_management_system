from django import forms


class PatientReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    condition = forms.CharField(max_length=100)
    ward = forms.CharField(max_length=100)
    disease = forms.CharField(max_length=100)