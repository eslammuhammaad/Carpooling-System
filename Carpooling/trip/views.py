from typing import final
from django.contrib import auth
from django.db.models.fields import DateField, TimeField
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import trip,Profile
import random
import operator
from math import sin, cos, sqrt, atan2, radians
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms.models import model_to_dict
from django.core import serializers
import json
from datetime import datetime
from django.contrib.auth import logout



def index(request):
    return render(request, 'trip/index.html')
    
def Home(request):
    return render(request, 'trip/Home.html')

def track(request):
    return render(request, 'trip/index.html')



def logout_view(request):
    logout(request)
    return redirect('Home')
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            number = request.POST.get('phoneNumber')
            trans = request.POST.get('trans')
            job = request.POST.get('job')
            gender = request.POST.get('gender')
            user = authenticate(username=username, password=password)
            login(request, user)
            userprofile = request.user.profile
            userprofile.phoneNumber = number
            userprofile.transportationMethod = trans
            userprofile.jobPosition = job
            userprofile.gender = gender
            userprofile.save()
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)


def getRecommendations(request):
    stpointLat = request.GET.get('stpointLat',0)    
    stpointLng = request.GET.get('stpointLng',0)
    endpointLat = request.GET.get('endPointLat',0)
    endpointLng = request.GET.get('endPointLng',0)
    stFloatLat = float(str(stpointLat))
    stFloatLng = float(str(stpointLng))
    endFloatLat = float(str(endpointLat))
    endFloatLng = float(str(endpointLng))

    current_user = request.user
    IDOFUSER=current_user.id
    #hna mfrood n filter el trips deh 
    startValues = trip.objects.values_list('startLatitude', 'startLongitude','userId')

    trainStart=startValues
    # add trip 
    # t = trip(startLongitude = stFloatLng, startLatitude = stFloatLat, endLongitude = endFloatLng, endLatitude = endFloatLat,
    #          startTime = datetime.now(), userId = request.user)
    # t.save()    
    testStart=[stFloatLat, stFloatLng,IDOFUSER]
    startOutput=getKNeighbors(trainStart,testStart,4)
    # w hna bardo 
    endValues = trip.objects.values_list('endLatitude', 'endLongitude','userId')
    trainEnd=endValues
    testEnd=[endFloatLat, endFloatLng,IDOFUSER]
    endOutput=getKNeighbors(trainEnd,testEnd,4)
    finalOutput=getCommon(startOutput,endOutput,IDOFUSER)
    phones = []
    transportation = []
    jobs = []
    gender = []
    users = []

    for x in finalOutput:
       user=(User.objects.all().filter(id = x[0]).values())
       users.append(list(user.values())) 
       num = Profile.objects.get(user=x)
       phones.append(num.phoneNumber)
       transportation.append(num.transportationMethod)
       jobs.append(num.jobPosition)
       gender.append(num.gender)

   
    return JsonResponse({'data':list(finalOutput),'phonenumber': phones, 
    'transportaion': transportation,
    'jobs': jobs,
    'gender': gender,
    'users': users,
    }, 
    safe=False)

def getCommon(list1,list2,IDOFUSER):
    intersaction = []
    for x in list1:
        for x2 in list2:
            if(x[0] == x2[0]):
                if(x[1] > 5):
                    continue
                intersaction.append((x[0],x[1],x2[1]))
                break
    return(intersaction)    

def euclideanDistance(instance1, instance2, length):
    distance = 0
    R = 6373.0
    lat1 = radians(instance1[0])
    lon1 = radians(instance1[1])
    lat2 = radians(instance2[0])
    lon2 = radians(instance2[1])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    result = R * c
    distance += result
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
        neighbors.append((distances[x][0][2], distances[x][1]))
    return neighbors