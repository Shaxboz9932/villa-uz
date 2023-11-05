from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import *

class ContactForm(forms.Form):

    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Subject...'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'row': 15, "placeholder": 'Your Message...'}))

class FullContactForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Your Name...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Mail...'}))
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Subject...'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'row': 15, "placeholder": 'Your Message...'}))


class AddVillaForm(forms.ModelForm):

    #category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={''}))
    #title = forms.CharField(widget=forms.TextInput())
    #slug = forms.SlugField(widget=forms.TextInput(attrs={'placeholder': 'title'}))
    class Meta:
        model = AllVilla
        fields = ('title', 'content', 'category', 'photo',
                  'author_name', 'author_phone_number', 'price',
                  'area', 'rooms', 'bathrooms', 'parking', 'floor'
                  )

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Ismingiz', widget=forms.TextInput())
    last_name = forms.CharField(label='Familiyangiz', widget=forms.TextInput())
    username = forms.CharField(label='Foydalanuvchi nomi', widget=forms.TextInput(), help_text='Обязательное поле. Не более 150 символов.')
    email = forms.EmailField(label='Elektron pochta', widget=forms.EmailInput())
    password1 = forms.CharField(label='Parolni kiriting', widget=forms.PasswordInput(), help_text="Пароль не должен быть слишком похож на другую вашу личную информацию.Ваш пароль должен содержать как минимум 8 символов.Пароль не должен быть слишком простым и распространенным.Пароль не может состоять только из цифр.")
    password2 = forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput(), help_text="Для подтверждения введите, пожалуйста, пароль ещё раз.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')