from django.shortcuts import render, redirect
from django.contrib.auth import login
from accaunts.forms import SignUpForm, ProfileForm, CommentForm
from accaunts.models import Profile,Comment


# Create your views here.
def logout_view(request):
    return render(request,'registration/logged_out.html',context={})
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={"form": form})

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'pages/profile.html', context={"profile": profile})

def profile_edit(request):
    user = request.user
    profile= Profile.objects.get(user=user)


    if request.method == "POST":
        user.username = request.POST.get('username')
        profile.name = request.POST.get('name')
        profile.surname = request.POST.get('surname')
        profile.bio = request.POST.get('bio')
        profile.birth_date = request.POST.get('birth_date')
        if request.FILES.get('img'):
            profile.img = request.FILES.get('img')
            profile.save()
        return redirect('profile')

    else:
        form = ProfileForm()

    context = {
        "profile": profile,
        "user": form
    }
    return render(request, 'profile_edit.html', context=context)


