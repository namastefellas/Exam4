from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import MyUserCreationForm
from django.contrib.auth.decorators import login_required

def login_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('album:photolist')
        context['has_error'] = True
    return render(request, 'login.html', context=context)


@login_required
def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('album:photolist')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            return redirect('album:photolist')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})