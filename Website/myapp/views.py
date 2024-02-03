from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
import random 
from django.contrib.auth.models import User
# Create your views here.
def home(request):
   motivational_quotes = [
    {"quote": "Believe you can and you're halfway there.", "said_by": "Theodore Roosevelt"},
    {"quote": "Your time is limited, don't waste it living someone else's life.", "said_by": "Steve Jobs"},
    {"quote": "The only way to do great work is to love what you do.", "said_by": "Steve Jobs"},
    {"quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "said_by": "Winston Churchill"},
    {"quote": "Don't watch the clock; do what it does. Keep going.", "said_by": "Sam Levenson"},
    {"quote": "The only place where success comes before work is in the dictionary.", "said_by": "Vidal Sassoon"},
    {"quote": "It's not about how hard you hit. It's about how hard you can get hit and keep moving.", "said_by": "Rocky Balboa"},
    {"quote": "The future belongs to those who believe in the beauty of their dreams.", "said_by": "Eleanor Roosevelt"},
    {"quote": "Success is stumbling from failure to failure with no loss of enthusiasm.", "said_by": "Winston Churchill"},
    {"quote": "The only limit to our realization of tomorrow will be our doubts of today.", "said_by": "Franklin D. Roosevelt"},
    {"quote": "You are never too old to set another goal or to dream a new dream.", "said_by": "C.S. Lewis"},
    {"quote": "The only person you are destined to become is the person you decide to be.", "said_by": "Ralph Waldo Emerson"},
    {"quote": "The only way to achieve the impossible is to believe it is possible.", "said_by": "Charles Kingsleigh (Alice in Wonderland)"},
    {"quote": "Success usually comes to those who are too busy to be looking for it.", "said_by": "Henry David Thoreau"},
    {"quote": "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", "said_by": "Christian D. Larson"},
    {"quote": "It always seems impossible until it's done.", "said_by": "Nelson Mandela"},
    {"quote": "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.", "said_by": "Roy T. Bennett"},
    {"quote": "Do not wait to strike till the iron is hot, but make it hot by striking.", "said_by": "William Butler Yeats"},
    {"quote": "Your life does not get better by chance, it gets better by change.", "said_by": "Jim Rohn"}
]
   num = random.randint(0,len(motivational_quotes)-1)
   quote = motivational_quotes[num]
   return render(request,'home.html',{"quotes":quote})

def register(request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request,"You have successfully signed in ")
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid details Please enter valid details")
                return redirect('signup')
        else :
             form = RegisterForm()
        return render(request,'signup.html',{"form":form})

         
    
def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form submission. Please check your inputs.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form})

def logoutView(request):
    logout(request)
    return redirect('home')

def userDetailsView(request):
    return render(request,'userDetails.html')

def listOfUsers(request):
    users = User.objects.all()

    return render(request,'listOfUsers.html',{'users':users})