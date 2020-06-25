from django.shortcuts import render, redirect
from django.views.generic import TemplateView , ListView
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team 
from .forms import AddTeam
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import TeamSerializer


def index(request):
    teams = Team.objects.order_by('-date_added').all()

    context = {'teams' : teams}

    return render(request, 'itsp/index.html', context)

def sign(request):
    if request.method == 'POST':
        form = AddTeam(request.POST)

        if form.is_valid():
            new_team = Team(name=request.POST['name'])
            new_team.save()
            new_id = Team(name=request.POST['t_id'])
            new_members = Team(name=request.POST['members'])

            return redirect('index')

    else:
        form = AddTeam()

    context = {'form' : form}
    return render(request, 'itsp/sign.html', context)

def details(request):
    teams = Team.objects.all()
    form=AddTeam() 
    context = {'teams' : teams ,'form' :form}
    return render(request, 'itsp/details.html' , context)

class TeamList(APIView):
    def get(self , request):
        Team1=Team.objects.all()
        serializer=TeamSerializer(Team1 , many=True)
        return Response(serializer.data)


    def post(self):
        pass

# Create your views here.
