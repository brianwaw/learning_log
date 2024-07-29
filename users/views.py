from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register a new User"""
    if request.method == 'POST':
        # PROCESS REGISTRATION FORM
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #log the new user into the system
            login(request, new_user)
            return redirect('learning_logs:all_topics')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
