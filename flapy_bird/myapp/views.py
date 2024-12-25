from django.shortcuts import render
from .models import Score

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'index.html')



from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Score

@login_required
def save_score(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        user = request.user
        Score.objects.create(user=user, score=score)
        return JsonResponse({"message": "Score saved!"})

from .models import Score

from django.shortcuts import render
from .models import Score

from django.shortcuts import render
from .models import Score

def leaderboard(request):
    # Get all scores grouped by user, ordered by the highest individual score
    all_scores = Score.objects.all().order_by('-score')
    scores_by_user = {}

    for score in all_scores:
        if score.user not in scores_by_user:
            scores_by_user[score.user] = []
        scores_by_user[score.user].append(score)

    return render(request, 'leaderboard.html', {'scores_by_user': scores_by_user})
