from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request): 
    if request.method == 'POST': 
        pass 
    else: 
        # user가 id와 password입력받는 빈 폼 
        form = CustomUserCreationForm()
    
    context = {
        'form': form, 
    }
    return render(request,'signup.html', context)