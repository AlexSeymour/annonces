from django.shortcuts import render, redirect, get_object_or_404
from user.forms import UserForm, ProfileForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from user.models import Profile


def CreateProfile(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()

            user.set_password(user.password)
            
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.add_message(request, messages.INFO, "Vous êtes désormais inscrit.")
            return redirect('/')


    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'registration/create.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def UpdateProfile(request):
    user_instance = request.user
    profile_instance = user_instance.profile


    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile_instance)
        user_form = UserUpdateForm(request.POST, instance=user_instance)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            # user = user_form.save(commit=False)


            user_form.save()

    else:
        profile_form = ProfileForm(instance=profile_instance)
        user_form = UserUpdateForm(instance=user_instance)

    return render(request, "account/profile.html", {'user_form':user_form, 'profile_form':profile_form})
