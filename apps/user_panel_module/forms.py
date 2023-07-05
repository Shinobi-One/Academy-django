from django import forms

from apps.user_module.models import User


class EditUserPanel(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','phone_number','about', 'avatar', ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',
                'name': 'message',
                'type': 'text'
            }),

            "last_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی',
                'name': 'message',
                'type': 'text'
            }),

            "username": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام کاربری',
                'name': 'message',
                'type': 'text'
            }),

            'email': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "ایمیل",
                'name': 'message',
                'type': "email"
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': "password",
                'placeholder': "رمـز عبـور",
            }),

            'phone_number': forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': "شماره همراه",
                'name': 'message',
                'type': "text"
            }),
            "about": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'درباره شما',
                'name': 'message',
                'type': 'text'
            }),
            'avatar': forms.FileInput(attrs={
                "class" : "form-control"
            })


        }
        labels = {
            'first_name': 'نام ',
            'last_name' : ' نام خانوادگی' ,
            'email': 'ایمیل',
            'phone_number': "شماره همراه" ,
            'password' : ' رمز عبور',
            'avatar': 'آواتار'
        }