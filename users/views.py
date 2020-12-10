from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from users.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        import json
        req_dict = json.loads(request.body)
        username = req_dict.get('username')
        password = req_dict.get('password')
        print(f'username : {username}   password: {password}')
        user = User.objects.create(username=username, password=password)
        # return HttpResponse('注册成功')
        # return JsonResponse({'message': '注册成功'})
        return redirect('/login/')


def login(request):
    username = request.session.get('username')
    if username:
        return HttpResponse(f'用户{username}已登录')
    if request.method == 'GET':
        # username = request.COOKIES.get('username', '')
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            if remember != 'true':
                request.session.set_expiry(0)
            response = JsonResponse({'message': 'login success'})
            # if remember == 'true':
            #     response.set_cookie('username', username, max_age=14 * 24 * 3600)
            return response


def user_info(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'})
    else:
        res_data = {
            'id': user.id,
            'name': user.username,
            'gender': user.gender,
            'age': user.age,
            'mobile': user.mobile,
        }
        return JsonResponse(res_data)
