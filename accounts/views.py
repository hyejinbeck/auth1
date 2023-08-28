from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login 

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

def login(request): 
    if request.method == 'POST': 
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid(): 
            # form인증이 되었다면, 
            # form의 get_user를 넣어주는 함수를 불러온다.
            auth_login(request, form.get_user() ) 
                                     # get_user 해당하는 아이디를 찾아서
                              # form에 불러와 
                       #요청값에 씌움
            #login으로 하겠다. 

            return redirect('accounts:login')
            

    else: 
        form = CustomAuthenticationForm()
    
    context = {
        'form':form,
    }
    return render(request, 'login.html', context)