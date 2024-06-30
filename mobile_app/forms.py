from django import forms
from .models import ShippingAddress, Customer


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'class': 'form-control ps-form__input'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control ps-form__input'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number',
        'class': 'form-control ps-form__input'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control ps-form__input'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control ps-form__input'
    }))

    class Meta:
        model = ShippingAddress
        fields = ['username', 'email', 'password', 'phone_number']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirmed_password = cleaned_data.get('confirm_password')

        if password != confirmed_password:
            raise forms.ValidationError(
                "Password doesn't match!"
            )


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User',
        'class': 'form-control ps-input'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number',
        'class': 'form-control ps-input'
    }))

    class Meta:
        model = ShippingAddress
        fields = ['username', 'phone_number']


class UserProfileForm(forms.ModelForm):

    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address',
        'class': 'form-control ps-input'
    }))

    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'City',
        'class': 'form-control ps-input'
    }))

    state = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'State',
        'class': 'form-control ps-input'
    }))

    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': 'Profile Picture',
        'class': 'form-control ps-input',
        'attrs': 'disabled'
    }))

    class Meta:
        model = UserForm
        fields = ['address', 'city', 'state', 'profile_picture']

