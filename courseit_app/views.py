from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Courses

# Create your views here.
def home(request):
    print(f"User: {request.user}, Is Authenticated: {request.user.is_authenticated}")
    return render(request, 'index.html')

def programs(request):
    courses = Courses.objects.all()
    print(courses)
    return render(request, 'programs.html',{"courses":courses})


def sign_up(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        created_username = email.replace("@gmail.com","")

        user = User.objects.filter(username=created_username)

        if user.exists():
            messages.info(request,"User Already Exists")
            return redirect("/sign_up/")
        
        user = User.objects.create_user(username=created_username,email=email)
        user.set_password(password)
        user.save()

        # Authenticate and log in the new user
        user = authenticate(request=request, username=created_username, password=password)
        if user is not None:
            login(request, user)  # Log in the user
            messages.info(request, "Account Successfully Created!")
            return redirect('/home/')
        else:
            messages.error(request, "An error occurred during login. Please try again.")
            return redirect('/login/')
    
    return render(request,"signup.html")

def logout_user(request):
    logout(request)
    return redirect('/login/')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(request=request,username=username,password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
        
    # Render the login page template (GET request)
    return render(request, 'login.html')



def course_info(request,course_id):

    course = get_object_or_404(Courses, id=course_id)


    sections = course.sections.all()

    course_data = []
    for section in sections:
        chapters = section.chapters.all()
        course_data.append(
            {"section":section,"chapters": chapters}
        )

    print(course_data)

    return render(request, 'course_info.html', {"course": course,"course_data":course_data})


def course_instruct(request,course_id):
    course = get_object_or_404(Courses, id=course_id)

    sections = course.sections.all()
    course_data = []
    for section in sections:
        chapters = section.chapters.all()
        course_data.append(
            {"section":section}
        )

    return render(request,"course_instructor.html", {"course_info" : course, "sections":course_data})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')