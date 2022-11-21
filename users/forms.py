from .models import *
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']
