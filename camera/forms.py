from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    DIST_CHOICES = (
	('a', 'Yunusabad'),
	('b', 'Chilanzar'),
	('c', 'Qibray'),
    )
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    district = forms.ChoiceField(required=False, choices=DIST_CHOICES, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','district','password1','password2',)
