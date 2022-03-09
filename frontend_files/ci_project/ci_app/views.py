from django.shortcuts import render
from ci_app.models.team_member import TeamMember
# Create your views here.

def about(request):
    team_list = TeamMember.objects.order_by('first_name')
    team_dict = {'team_member': team_list}
    return render(request,'about.html',team_dict)


def home(request):
    return render(request,'home.html')

def buy(request):
    return render(request,'buy.html')

def contactUs(request):
    return render(request,'contactUs.html')

def history(request):
    return render(request,'history.html')

def recommend(request):
    return render(request,'recommend.html')

def refund(request):
    return render(request,'refund.html')