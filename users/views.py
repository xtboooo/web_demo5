from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from users.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'username : {username}   password: {password}')
        user = User.objects.create(username=username, password=password)
        # return HttpResponse('注册成功')
        # return JsonResponse({'message': '注册成功'})
        return redirect('/login/')


def login(request):
    return render(request, 'login.html')
