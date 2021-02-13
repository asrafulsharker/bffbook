from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    hello = 'hello nirob'
    context = {
        'user_t': user,
        'hello': hello,
    }
    # return HttpResponse('Hello Nirob')
    return render(request, 'main/home.html',context)