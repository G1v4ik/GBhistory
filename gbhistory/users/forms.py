from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')
    
    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email
    

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": '*Login'})
            self.fields['email'].widget.attrs.update({"placeholder": '*Email'})
            self.fields['first_name'].widget.attrs.update({"placeholder": '*Name'})
            self.fields["last_name"].widget.attrs.update({"placeholder": '*Last Name'})
            self.fields['password1'].widget.attrs.update({"placeholder": '*Password'})
            self.fields['password2'].widget.attrs.update({"placeholder": '*Password again'})
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields[field].help_text = None
            self.fields[field].label = ""
        
    

class UserLoginForm(AuthenticationForm):
    """
    Форма авторизации на сайте
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Login'
            self.fields['password'].widget.attrs['placeholder'] = 'Password'
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].help_text = None
            self.fields[field].label = ""

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('about_you',)

#     def __init__(self, *args, **kwargs):
#         """
#         Обновление стилей формы обновления
#         """
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control',
#                 'autocomplete': 'off'
#             })