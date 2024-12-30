from .models import Question, Level
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre l'utilisateur dans la base de données
            messages.success(request, "Compte créé avec succès !")
            return redirect('login')  # Redirige vers la page de connexion
        else:
            messages.error(request, "Une erreur s'est produite. Veuillez vérifier le formulaire.")
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


#@login_required
def home(request):
    return render(request, 'home.html')


def selectlevel(request):
    levels = Level.objects.all()
    return render(request, 'selectlevel.html', {'levels' : levels})


def start(request, level_id):
    level = Level.objects.get(id=level_id)  # Récupère le niveau par ID
    questions = Question.objects.filter(level=level)  # Filtrer les questions par niveau
    return render(request, 'start.html', {'questions': questions, 'level': level})


def result(request):
    correct_answers = 0
    total_questions = len(request.POST) - 1

    for key, value in request.POST.items():
        if value == 'correct':
            correct_answers += 1

    return render(request, 'result.html', {'correct_answers': correct_answers, 'total_questions': total_questions})


def community(request):
    return render(request, 'community.html')