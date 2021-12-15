from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import trip,Member
import random
import operator
from math import sin, cos, sqrt, atan2, radians


def index(request):
    return render(request, 'trip/index.html')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def getRecommendations(request):
   startValues = trip.objects.values_list('startLatitude', 'startLongitude','userId')
   trainStart=startValues
   testStart=[12,4,1]
   startOutput=getKNeighbors(trainStart,testStart,3)
   endValues = trip.objects.values_list('endLatitude', 'endLongitude','userId')
   trainEnd=endValues
   testEnd=[12,4,1]
   endOutput=getKNeighbors(trainEnd,testEnd,3)
   finalOutput=getCommon(startOutput,endOutput)
   return HttpResponse(finalOutput)

def getCommon(list1,list2):
    list1_as_set = set(list1)
    intersection = list1_as_set.intersection(list2)
    intersection_as_list = list(intersection)
    return(intersection_as_list)

    
def euclideanDistance(instance1, instance2, length):
    distance = 0
    R = 6373.0
    lat1 = radians(instance1[0])
    lon1 = radians(instance1[1])
    lat2 = radians(instance2[0])
    lon2 = radians(instance2[1])
    print(instance1[0], instance1[1])
    print(instance2[0], instance2[1])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)*2 + cos(lat1) * cos(lat2) * sin(dlon / 2)*2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    result = R * c
    distance += result
    print(distance)
    return distance

def getKNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist,trainingSet[2]))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0][2])
    return neighbors