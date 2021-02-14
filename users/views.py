from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateform, ProfileUpdateform
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно зарегистрирован')
            return redirect('home')
    else:
        form = UserRegisterForm()
    data = {
        'title': 'Cтраница регистрации',
        'form': form,
    }
    return render(request,'users/reg.html',data)


@login_required
def profile(request):
    return render(request,'users/profile.html')

@login_required
def profile_update(request):
    if request.method == "POST":
        profileForm = ProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)
        updateUserForm = UserUpdateform(request.POST,instance=request.user)

        if profileForm.is_valid() and updateUserForm.is_valid():
            profileForm.save()
            updateUserForm.save()
            messages.success(request, f'Ваши данные были успешно обновлены')
            return redirect('profile')

    else:
        profileForm = ProfileUpdateform(instance=request.user.profile)
        updateUserForm = UserUpdateform(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }
    return render(request,'users/profile_update.html',data)