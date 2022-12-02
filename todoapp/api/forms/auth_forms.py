
from django import forms
from django.core.exceptions import ValidationError

from api.models import User


class RegistrationForm(forms.Form):

    def email_valid(value):
        
        user_email = User.objects.filter(email = value).first()
        
        if user_email :
            raise ValidationError("Email already registered")

    def phone_valid(value):

        user_phone = User.objects.filter(phone = value).first()

        if user_phone:
            raise ValidationError("Phone number already registered")

    name = forms.CharField(max_length= 255)
    email = forms.EmailField(validators= [email_valid])
    phone = forms.IntegerField(validators= [phone_valid])
    password = forms.CharField(max_length= 255)

    class Meta:

        name = {
            "required": True,
        }
        email = {
            "required": True,
        }
        phone = {
            "required": True,
        }
        password = {
            "required": True,
        }
        
class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField()

    class Meta:

        email = {
            "required": True,
        }
        password = {
            "required": True,
        }

class UpdatePasswordForm(forms.Form):
    
    current_pass = forms.CharField()
    new_pass = forms.CharField()
    confirm_pass = forms.CharField()

    class Meta:

        current_pass = {
            "required": True,
        }
        new_pass = {
            "required": True,
        }
        confirm_pass = {
            "required": True,
        }
