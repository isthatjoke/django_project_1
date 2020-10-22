from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import ShopUser
from django.contrib.auth.forms import forms
import random, hashlib


class ShopUserLoginForm(AuthenticationForm):
    required_fields = ['username', 'password']

    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in self.required_fields:
                field.help_text = '* required'
            else:
                field.help_text = ''


class ShopUserRegisterForm(UserCreationForm):
    required_fields = ['username', 'email', 'age', 'password1', 'password2']

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in self.required_fields:
                field.help_text = '* required'
            else:
                field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Dude! you're too young!")

        return data

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and ShopUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Dude! that mail has been already registered")

        return email

    def save(self):
        user = super(ShopUserRegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()
        user.save()
        return user


class ShopUserEditForm(UserChangeForm):
    required_fields = ['username', 'email', 'age', 'password']

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in self.required_fields:
                field.help_text = '* required'
            else:
                field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Dude! you're too young!")

        return data
