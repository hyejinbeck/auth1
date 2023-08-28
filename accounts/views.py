from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('accounts:signup')


    else: 
        # user가 id와 password입력받는 빈 폼 
        form = CustomUserCreationForm()
    
    context = {
        'form': form, 
    }
    return render(request,'signup.html', context)