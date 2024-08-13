from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS,'Oturum açıldı')
            # print('login başarılı')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR,'Hatalı username yada parola')
            # print('kullanıcı adı veya parola yanlış')
            return redirect('login')
    else:
        return render(request,'user/login.html')

def register(request):
    if request.method == "POST":
        
        # get from values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.WARNING, 'Bu kulanıcı adı daha önce alınmış')
                # print('bu kullanıcı adı daha önce alınmış')
                return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.add_message(request, messages.WARNING,'Bu mail daha önce alınmış')
                # print('parololar eşleşmiyor')
                return redirect('register')
            else:
                # herşey güzel
                user = User.objects.create_superuser(username=username, password=password, email=email)
                
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Hesabınız oluşturuldu')
                # print('kullanıcı oluşturuldu')
                return redirect('login')
            
    else:
        return render(request,'user/register.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS,'Oturumunuz kapatıldı')
    return redirect('index')
