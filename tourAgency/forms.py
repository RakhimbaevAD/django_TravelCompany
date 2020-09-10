from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Reviews, Orders


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ReviewForm(forms.ModelForm):
    '''Форма отзывов'''
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class OrderForm(forms.ModelForm):
    '''Форма бронирования'''
    class Meta:
        model = Orders
        fields = ('email', 'phone_number', 'food_type', 'days_number', 'persons_number', 'departure_date')