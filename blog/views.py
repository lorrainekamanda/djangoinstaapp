from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import registrationForm,UpdateUser,UpdateProfile,PostForm
from django.contrib.auth.models import User
from .models import Image,Profile
# from .models import Post


@login_required
def home(request):
    context = {
        'users':User.objects.all(),
        'images':Image.objects.all(),
    }

    return render(request,'blog/home.html',context)


def register(request):
    if request.method == 'POST':
       form = registrationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request,f'Account created for {username}')
           return redirect('blog-home')

    else:
       form = registrationForm()
    return render (request,'blog/register.html',{'form':form})


def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'blog/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searches/search.html',{"message":message})

@login_required
def profile(request):
    if request.method == 'POST':

       user_form = UpdateUser(request.POST,instance=request.user)
       profile_form = UpdateProfile(request.POST,request.FILES,instance = request.user.profile)
       
       if user_form.is_valid() and profile_form.is_valid():
           user_form.save()
           profile_form.save()
           
           messages.success(request,f'Account updated')
           return redirect('blog-profile')
    else:
       user_form = UpdateUser(instance=request.user)
       profile_form = UpdateProfile(instance = request.user.profile)
       
    context = {
        'user_form':user_form,
        'profile_form': profile_form,
        
        
        
       }
    return render(request,'blog/profile.html',context )

def post():
    if request.method == 'POST':
        post_form = PostForm(request.Image,request.FILES,instance = request.user.image)
        if post_form.is_valid():
            post_form.save()
            messages.success(request,f'Content Uploaded')
            return redirect('blog-profile')
    else:
        post_form = PostForm(request.Image,request.FILES,instance = request.user.image)
    context = {
       'post_form': post_form,
      
    }
    return render(request,'blog/profile.html',context )



