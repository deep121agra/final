from django import forms
from .models import User,UserProfile
from .validators import allow_only_images_validator
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
class UserProfileForm(forms.ModelForm):
    adress=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Start tyuing...','required':'required'}))
    #profile_picture=forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])
    #cover_photo=forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model=UserProfile
        fields=['profile_picture','cover_photo','adress','country','state','city','pin_code','latitute','longitude']

    def __init__(self,*args,**kwargs):
        super(UserProfileForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field=='latitute' or field=='longitude':
                self.fields[field].widget.attrs['readonly']='readonly'
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone_number']                
        
