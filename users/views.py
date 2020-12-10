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
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'login.html', locals())
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            response = JsonResponse({'message': 'login success'})
            if remember == 'true':
                response.set_cookie('username', username, max_age=14 * 24 * 3600)
            return response
