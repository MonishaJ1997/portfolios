from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def home(request):
    skills = ["Python", "Django", "HTML", "CSS", "JavaScript"]
    return render(request, "home.html", {"skills": skills})

def about(request):
    return render(request, "about.html")

def projects(request):
    projects = [
        {"name": "E-commerce Website", "desc": "Built with Django & Bootstrap"},
        {"name": "Blog App", "desc": "Flask + SQLite"},
        {"name": "Portfolio", "desc": "This website itself"},
    ]
    return render(request, "projects.html", {"projects": projects})

def contact(request):
    return render(request, "contact.html")
