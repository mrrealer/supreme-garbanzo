from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from abcproject.models import Profile

def save_prospect_info(request):
    #Save stuff
    
    return render(request, 'abcproject/index.html', {})


def index(request):
    return render(request, 'abcproject/index.html', {})

def home(request):
    return render(request, 'abcproject/home.html', {})


def profile(request):
    # return render(request, 'abcproject/profile.html',{})
    if request.user.is_authenticated(): 
        u = request.user
        if request.method == 'GET' or request.method != 'POST':
            return render(request, 'abcproject/profile.html', {'user': u}) 
        else:
            print request.POST
            user_id = request.user.pk
            user_profile = Profile.objects.filter(user=user_id)
            
            if user_profile:
                user_profile[0].interests = request.POST['interests']
                user_profile[0].photo = request.POST['picture']
                user_profile[0].save()
                return HttpResponse("Profile updated.")
            else:
                p = Profile(user=request.user, interests=request.POST['interests'], photo=request.POST['picture'])
                p.save()
                return HttpResponse("Profile made.")

    else:
        return redirect('/login')


def register(request):
    #If user is not attempting to POST with their request, load up the register webpage
    print request.user
    if request.method == 'GET' or request.method != 'POST':
        return render(request, 'abcproject/register.html', {})

    #Otherwise, print user's post request to the terminal log
    # print request.POST
    #Create a new user using built in django user libraries, pulling information from their POST request
    user = User.objects.create_user(username = request.POST['user_name'], email = request.POST['email'], password = request.POST['password'])
    #If we are not successful in generating a user, reload the register webpage.
    # if not user:
    #    return render(request, 'abcproject/register.html', {})
    #Otherwise, we save the new user instance
    # user.save()
    # #And then we log the user in.
    user = authenticate(username=request.POST['user_name'],password=request.POST['password'])
    login(request, user)
    # #Finally, we redirect to the homepage if we were successful in registering a new user. There is now a logged in user.
    print request.user
    return redirect('/')


def login_user(request):
    print request.user
    if request.method == 'GET' or request.method != 'POST':
       return render(request, 'abcproject/login_user.html', {})

    user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

    if not user:
       return redirect('/login/')

    login(request, user)
    print request.user
    return redirect('/')

def logout_user(request):
    logout(request)
    
    return redirect('/')

