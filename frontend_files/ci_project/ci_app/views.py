from django.shortcuts import render
from ci_app.models.team_member import TeamMembers
# Create your views here.

def about(request):
    return render(request,'about.html')


def home(request):
    return render(request,'home.html')