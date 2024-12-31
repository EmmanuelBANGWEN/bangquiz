# from .models import Question, Level
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForms, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import RegistrationForms
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)

            return redirect('login')  # Redirige vers la page de connexion
        else:
            messages.error(request, "Une erreur s'est produite. Veuillez vérifier le formulaire.")
    else:
        form = RegistrationForms()
    return render(request, 'register.html', {'form': form})
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get("username")  # Utilisation de .get() pour éviter l'exception
            password = request.POST.get("password")  # Utilisation de .get() pour éviter l'exception

            # Vérification que les champs sont remplis
            if not username or not password:
                messages.error(request, "Nom d'utilisateur et mot de passe sont requis.")
                return render(request, 'login.html')

            # Tentative de connexion
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('login')


#@login_required
def home(request):
    return render(request, 'home.html')


levels = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}


questions = [
    {"id": 1, "question": "Quelle fonction permet d'afficher un message à l'écran en Python ?", "level_id": 1},
    {"id": 2, "question": "Comment déclare-t-on une variable en Python ?", "level_id": 1},
    {"id": 4, "question": "Quel est le type de la variable suivante ? x = \"Bonjour\"", "level_id": 1},
    {"id": 5, "question": "Que fait cette expression ? x = 10 + 5", "level_id": 1},
    {"id": 6, "question": "Quel est le résultat de 3 + 4 en Python ?", "level_id": 1},
    {"id": 7, "question": "Quel est le type de la variable suivante ? x = [1, 2, 3]", "level_id": 1},
    {"id": 8, "question": "Comment ajoutons-nous un élément à la fin d'une liste en Python ?", "level_id": 1},
    {"id": 9, "question": "Que fait la fonction len() en Python ?", "level_id": 1},
    {"id": 10, "question": "Quel opérateur est utilisé pour l'addition en Python ?", "level_id": 1},
    {"id": 11, "question": "Quel type de données est retourné par la fonction input() ?", "level_id": 2},
    {"id": 12, "question": "Que fait my_dict.keys() sur un dictionnaire ?", "level_id": 2},
    {"id": 13, "question": "Comment lire un fichier en Python ?", "level_id": 2},
    {"id": 14, "question": "Que fait la méthode `split()` en Python ?", "level_id": 2},
    {"id": 15, "question": "Quelle est la syntaxe correcte pour un if en Python ?", "level_id": 2},
    {"id": 17, "question": "Que fait la méthode `upper()` en Python ?", "level_id": 2},
    {"id": 18, "question": "Que fait la méthode split() sur une chaîne de caractères ?", "level_id": 2},
    {"id": 19, "question": "Quel est le résultat de [1, 2, 3] * 2 ?", "level_id": 2},
    {"id": 20, "question": "Quel mot-clé est utilisé pour définir une classe en Python ?", "level_id": 2},
    {"id": 21, "question": "Quel est le type de la variable suivante ? x = 10 / 2", "level_id": 2},
    {"id": 22, "question": "Que fait la fonction map() en Python ?", "level_id": 3},
    {"id": 23, "question": "Comment définir une fonction lambda ?", "level_id": 3},
    {"id": 24, "question": "Que fait le décorateur @staticmethod ?", "level_id": 3},
    {"id": 25, "question": "Que fait le mot-clé yield en Python ?", "level_id": 3},
    {"id": 26, "question": "Que fait la méthode __init__ dans une classe Python ?", "level_id": 3},
    {"id": 27, "question": "Que permet de faire le module os en Python ?", "level_id": 3},
    {"id": 28, "question": "Quelle structure de données est immuable ?", "level_id": 3},
    {"id": 29, "question": "Que fait la fonction zip() en Python ?", "level_id": 3},
    {"id": 30, "question": "Quelle bibliothèque est utilisée pour le traitement des données en Python ?", "level_id": 3},
    {"id": 31, "question": "Quel est le résultat de cette expression ? x = 2 ** 3", "level_id": 3},
    {"id": 32, "question": "Quel symbole est utilisé pour les commentaires en Python ?", "level_id": 1}
]



answers = [
    {"id": 1, "answer": "A) echo()", "is_correct": False, "question_id": 1},
    {"id": 2, "answer": "B) output()", "is_correct": False, "question_id": 1},
    {"id": 3, "answer": "C) print()", "is_correct": True, "question_id": 1},
    {"id": 4, "answer": "D) show()", "is_correct": False, "question_id": 1},
    {"id": 5, "answer": "A) x = 5", "is_correct": True, "question_id": 2},
    {"id": 6, "answer": "B) var x = 5", "is_correct": False, "question_id": 2},
    {"id": 7, "answer": "C) int x = 5", "is_correct": False, "question_id": 2},
    {"id": 8, "answer": "D) let x = 5", "is_correct": False, "question_id": 2},
    {"id": 9, "answer": "A) int", "is_correct": False, "question_id": 4},
    {"id": 10, "answer": "B) str", "is_correct": True, "question_id": 4},
    {"id": 11, "answer": "C) bool", "is_correct": False, "question_id": 4},
    {"id": 12, "answer": "D) list", "is_correct": False, "question_id": 4},
    {"id": 13, "answer": "A) Affiche 10", "is_correct": False, "question_id": 5},
    {"id": 14, "answer": "B) Crée une liste avec 10 et 5", "is_correct": False, "question_id": 5},
    {"id": 15, "answer": "C) Assigne 15 à x", "is_correct": True, "question_id": 5},
    {"id": 16, "answer": "D) Crée une erreur", "is_correct": False, "question_id": 5},
    {"id": 17, "answer": "A) 34", "is_correct": False, "question_id": 6},
    {"id": 18, "answer": "B) 12", "is_correct": False, "question_id": 6},
    {"id": 19, "answer": "C) 7", "is_correct": True, "question_id": 6},
    {"id": 20, "answer": "D) Erreur", "is_correct": False, "question_id": 6},
    {"id": 21, "answer": "A) int", "is_correct": False, "question_id": 7},
    {"id": 22, "answer": "B) float", "is_correct": False, "question_id": 7},
    {"id": 23, "answer": "C) list", "is_correct": True, "question_id": 7},
    {"id": 24, "answer": "D) str", "is_correct": False, "question_id": 7},
    {"id": 25, "answer": "A) list.push(1)", "is_correct": False, "question_id": 8},
    {"id": 26, "answer": "B) list.append(1)", "is_correct": True, "question_id": 8},
    {"id": 27, "answer": "C) list.add(1)", "is_correct": False, "question_id": 8},
    {"id": 28, "answer": "D) list.insert(1)", "is_correct": False, "question_id": 8},
    {"id": 29, "answer": "A) Elle retourne la longueur d'un nombre", "is_correct": False, "question_id": 9},
    {"id": 30, "answer": "B) Elle retourne la longueur d'une chaîne de caractères ou d'une liste", "is_correct": True, "question_id": 9},
    {"id": 31, "answer": "C) Elle supprime un élément d'une liste", "is_correct": False, "question_id": 9},
    {"id": 32, "answer": "D) Elle crée une nouvelle liste", "is_correct": False, "question_id": 9},
    {"id": 33, "answer": "A) +", "is_correct": True, "question_id": 10},
    {"id": 34, "answer": "B) -", "is_correct": False, "question_id": 10},
    {"id": 35, "answer": "C) *", "is_correct": False, "question_id": 10},
    {"id": 36, "answer": "D) /", "is_correct": False, "question_id": 10},
    {"id": 37, "answer": "A) int", "is_correct": False, "question_id": 11},
    {"id": 38, "answer": "B) string", "is_correct": True, "question_id": 11},
    {"id": 39, "answer": "C) float", "is_correct": False, "question_id": 11},
    {"id": 40, "answer": "D) bool", "is_correct": False, "question_id": 11},
    {"id": 41, "answer": "A) Retourne les clés", "is_correct": True, "question_id": 12},
    {"id": 42, "answer": "B) Retourne les valeurs", "is_correct": False, "question_id": 12},
    {"id": 43, "answer": "C) Retourne les paires clés-valeurs", "is_correct": False, "question_id": 12},
    {"id": 44, "answer": "D) Supprime les clés", "is_correct": False, "question_id": 12},
    {"id": 45, "answer": "A) open('file.txt')", "is_correct": True, "question_id": 13},
    {"id": 46, "answer": "B) file.open('file.txt')", "is_correct": False, "question_id": 13},
    {"id": 47, "answer": "C) openFile('file.txt')", "is_correct": False, "question_id": 13},
    {"id": 48, "answer": "D) read('file.txt')", "is_correct": False, "question_id": 13},
    {"id": 49, "answer": "A) Elle divise une chaîne de caractères en une liste de sous-chaînes", "is_correct": True, "question_id": 14},
    {"id": 50, "answer": "B) Elle joint plusieurs chaînes de caractères", "is_correct": False, "question_id": 14},
    {"id": 51, "answer": "C) Elle supprime les espaces blancs", "is_correct": False, "question_id": 14},
    {"id": 52, "answer": "D) Elle remplace un caractère par un autre", "is_correct": False, "question_id": 14},
    {"id": 53, "answer": "A) if x > 0:", "is_correct": True, "question_id": 15},
    {"id": 54, "answer": "B) if (x > 0)", "is_correct": False, "question_id": 15},
    {"id": 55, "answer": "C) if x > 0 then", "is_correct": False, "question_id": 15},
    {"id": 56, "answer": "D) if x > 0 {}", "is_correct": False, "question_id": 15},
    {"id": 61, "answer": "A) Elle convertit une chaîne de caractères en majuscules", "is_correct": True, "question_id": 17},
    {"id": 62, "answer": "B) Elle convertit une chaîne de caractères en minuscules", "is_correct": False, "question_id": 17},
    {"id": 63, "answer": "C) Elle ajoute un caractère à la fin de la chaîne", "is_correct": False, "question_id": 17},
    {"id": 64, "answer": "D) Elle supprime les espaces blancs", "is_correct": False, "question_id": 17},
    {"id": 65, "answer": "A) Fusionne les chaînes", "is_correct": False, "question_id": 18},
    {"id": 66, "answer": "B) Divise une chaîne", "is_correct": True, "question_id": 18},
    {"id": 67, "answer": "C) Inverse une chaîne", "is_correct": False, "question_id": 18},
    {"id": 68, "answer": "D) Compte les caractères", "is_correct": False, "question_id": 18},
    {"id": 69, "answer": "A) [1, 2, 3, 1, 2, 3]", "is_correct": True, "question_id": 19},
    {"id": 70, "answer": "B) [2, 4, 6]", "is_correct": False, "question_id": 19},
    {"id": 71, "answer": "C) [1, 2, 3, 3, 2, 1]", "is_correct": False, "question_id": 19},
    {"id": 72, "answer": "D) Erreur", "is_correct": False, "question_id": 19},
    {"id": 73, "answer": "A) function", "is_correct": False, "question_id": 20},
    {"id": 74, "answer": "B) class", "is_correct": True, "question_id": 20},
    {"id": 75, "answer": "C) def", "is_correct": False, "question_id": 20},
    {"id": 76, "answer": "D) object", "is_correct": False, "question_id": 20},
    {"id": 77, "answer": "A) int", "is_correct": False, "question_id": 21},
    {"id": 78, "answer": "B) float", "is_correct": True, "question_id": 21},
    {"id": 79, "answer": "C) str", "is_correct": False, "question_id": 21},
    {"id": 80, "answer": "D) list", "is_correct": False, "question_id": 21},
    {"id": 81, "answer": "A) Elle applique une fonction à tous les éléments d'un itérable", "is_correct": True, "question_id": 22},
    {"id": 82, "answer": "B) Elle filtre les éléments d'un itérable", "is_correct": False, "question_id": 22},
    {"id": 83, "answer": "C) Elle trie un itérable", "is_correct": False, "question_id": 22},
    {"id": 84, "answer": "D) Elle combine deux listes", "is_correct": False, "question_id": 22},
    {"id": 85, "answer": "A) def lambda(x): x + 1", "is_correct": False, "question_id": 23},
    {"id": 86, "answer": "B) lambda x: x + 1", "is_correct": True, "question_id": 23},
    {"id": 87, "answer": "C) lambda(x) {x + 1}", "is_correct": False, "question_id": 23},
    {"id": 88, "answer": "D) x => x + 1", "is_correct": False, "question_id": 23},
    {"id": 89, "answer": "A) Définit une méthode statique", "is_correct": True, "question_id": 24},
    {"id": 90, "answer": "B) Définit une méthode privée", "is_correct": False, "question_id": 24},
    {"id": 91, "answer": "C) Crée une variable statique", "is_correct": False, "question_id": 24},
    {"id": 92, "answer": "D) Gère les exceptions", "is_correct": False, "question_id": 24},
    {"id": 93, "answer": "A) Il retourne une valeur d'une fonction sans l'arrêter", "is_correct": True, "question_id": 25},
    {"id": 94, "answer": "B) Il crée une boucle infinie", "is_correct": False, "question_id": 25},
    {"id": 95, "answer": "C) Il crée une variable globale", "is_correct": False, "question_id": 25},
    {"id": 96, "answer": "D) Il définit une classe", "is_correct": False, "question_id": 25},
    {"id": 97, "answer": "A) Crée une instance", "is_correct": False, "question_id": 26},
    {"id": 98, "answer": "B) Détruit une instance", "is_correct": False, "question_id": 26},
    {"id": 99, "answer": "C) Initialise une instance", "is_correct": True, "question_id": 26},
    {"id": 100, "answer": "D) Copie une instance", "is_correct": False, "question_id": 26},
    {"id": 101, "answer": "A) Gérer les fichiers et les répertoires du système", "is_correct": True, "question_id": 27},
    {"id": 102, "answer": "B) Gérer la mémoire", "is_correct": False, "question_id": 27},
    {"id": 103, "answer": "C) Gérer les entrées/sorties", "is_correct": False, "question_id": 27},
    {"id": 104, "answer": "D) Gérer les exceptions", "is_correct": False, "question_id": 27},
    {"id": 105, "answer": "A) Liste", "is_correct": False, "question_id": 28},
    {"id": 106, "answer": "B) Dictionnaire", "is_correct": False, "question_id": 28},
    {"id": 107, "answer": "C) Tuple", "is_correct": True, "question_id": 28},
    {"id": 108, "answer": "D) Ensemble", "is_correct": False, "question_id": 28},
    {"id": 109, "answer": "A) Elle combine deux ou plusieurs listes élément par élément", "is_correct": True, "question_id": 29},
    {"id": 110, "answer": "B) Elle compresse les éléments d'une liste", "is_correct": False, "question_id": 29},
    {"id": 111, "answer": "C) Elle trie les éléments d'une liste", "is_correct": False, "question_id": 29},
    {"id": 112, "answer": "D) Elle crée une nouvelle liste", "is_correct": False, "question_id": 29},
    {"id": 113, "answer": "A) numpy", "is_correct": False, "question_id": 30},
    {"id": 114, "answer": "B) pandas", "is_correct": True, "question_id": 30},
    {"id": 115, "answer": "C) matplotlib", "is_correct": False, "question_id": 30},
    {"id": 116, "answer": "D) flask", "is_correct": False, "question_id": 30},
    {"id": 117, "answer": "A) 6", "is_correct": False, "question_id": 31},
    {"id": 118, "answer": "B) 8", "is_correct": True, "question_id": 31},
    {"id": 119, "answer": "C) 9", "is_correct": False, "question_id": 31},
    {"id": 120, "answer": "D) 5", "is_correct": False, "question_id": 31},
    {"id": 121, "answer": "A) //", "is_correct": False, "question_id": 32},
    {"id": 122, "answer": "B) <!-- -->", "is_correct": False, "question_id": 32},
    {"id": 123, "answer": "C) #", "is_correct": True, "question_id": 32},
    {"id": 124, "answer": "D) /* */", "is_correct": False, "question_id": 32}
]






# def selectlevel(request):
#     levels = Level.objects.all()
#     return render(request, 'selectlevel.html', {'levels' : levels})

def selectlevel(request):
    levels = {
        1: "Easy",
        2: "Medium",
        3: "Hard"
    }
    return render(request, 'selectlevel.html', {'levels': levels})


# from django.shortcuts import render

# # Importez les données (niveaux, questions, réponses)
# levels = {
#     1: "Easy",
#     2: "Medium",
#     3: "Hard"
# }

# questions = [
#     {"id": 1, "question": "Quelle fonction permet d'afficher un message Ã  l'Ã©cran en Python ?", "level_id": 1},
#     {"id": 2, "question": "Comment dÃ©clare-t-on une variable en Python ?", "level_id": 1},
#     # ... Ajoutez ici toutes les autres questions
# ]

# answers = [
#     {"id": 1, "answer": "A) echo()", "is_correct": False, "question_id": 1},
#     {"id": 2, "answer": "B) output()", "is_correct": False, "question_id": 1},
#     # ... Ajoutez ici toutes les autres réponses
# ]
def start(request, level_id):
    # Filtrer les questions en fonction du niveau choisi
    filtered_questions = [q for q in questions if q['level_id'] == level_id]
    
    # Trouver les réponses correspondantes aux questions filtrées
    questions_with_answers = []
    for question in filtered_questions:
        question_answers = [a for a in answers if a['question_id'] == question['id']]
        questions_with_answers.append({'question': question, 'answers': question_answers})

    # Récupérer le nom du niveau pour l'affichage
    level_name = levels.get(level_id, "Niveau inconnu")

    return render(request, 'start.html', {
        'questions_with_answers': questions_with_answers,
        'level_name': level_name
    })



def result(request):
    correct_answers = 0
    total_questions = len(request.POST) - 1

    for key, value in request.POST.items():
        if value == 'correct':
            correct_answers += 1

    return render(request, 'result.html', {'correct_answers': correct_answers, 'total_questions': total_questions})


def community(request):
    return render(request, 'community.html')