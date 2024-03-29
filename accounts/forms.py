from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import User 

class CustomUserCreationForm(UserCreationForm): 
    
    class Meta: 
        model = User 
        #fields = '__all__'
        fields = ('username',)

class CustomAuthenticationForm(AuthenticationForm): 
    pass 