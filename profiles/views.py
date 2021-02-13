from django.shortcuts import render
from  .models import Profile
# Create your views here.


def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)

    context ={
        'profile': profile,
    }

    return render(request,'profiles/myprofile.html',context)

 