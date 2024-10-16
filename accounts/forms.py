from django import forms
from .models import User
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['firstname','lastname','username','email','phone_number','password']



    def clean(self):
        cleand_data=super(UserForm,self).clean()
        password=cleand_data.get('password')
        confirm_password=cleand_data.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError("password does not match")
        
