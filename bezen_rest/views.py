from django.db import connection
from django.shortcuts import redirect, render
from .models import Fish
from .models import ProcessedFish
import json
from django.http import HttpResponse
import requests
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import django.template.loader
from .forms import ImageForm 
import os

import numpy as np
import cv2


import threading

import base64
from datetime import datetime
@csrf_exempt
def addrecord(request):

    
    if(request.method=='POST'):
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():

            newfish = Fish()
            obj = ProcessedFish()
            newfish.fish_name = request.POST.get('fish_name')
            newfish.fish_species = request.POST.get('fish_species')
            newfish.weight =request.POST.get('weight')
            newfish.length =request.POST.get('length')
            newfish.lattitude =request.POST.get('lattitude')
            newfish.longitude =request.POST.get('longitude')
            
            if len(request.FILES)!=0:
                newfish.img = request.FILES['img']
                
            
            newfish.save()
            path = "images/"+str(request.FILES['img'])
            obj.fish_id = newfish.fish_id
            obj.img_name = path
            obj.is_Resized =False
            obj.save()


        return HttpResponse("record added")
    return render(request, './index.html')




def schedule(request):
    if(request.method=='GET'):
        path = "media/"
        resp=[]
        fishes = Fish.objects.all().order_by("timestamp")
        for fish in fishes:
            obj = ProcessedFish.objects.get(fish_id = fish.fish_id)
            
            if (obj.is_Resized==False):
                try:
                  process_image(cv2.imread(path+obj.img_name),140,140,fish)
                except Exception:
                  t = threading.Thread(process_image, (cv2.imread(path+obj.img_name),140,140,fish))
                  t.start()

                obj.is_Resized = True
                obj.img_name=str("resized_images/"+str(fish.fish_id)+".png")
                obj.save()
        for fish in ProcessedFish.objects.all():
                resp.append({"Fish id":fish.fish_id,"Resized":str(fish.is_Resized)})

        return HttpResponse(json.dumps(resp))


def get_processed_image (request,id):
    if (request.method == 'GET'):
        print("id", id)
        image_path = "media/resized_images/"+str(id)

        
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    ctx={}
    ctx["image"] = image_data
    return render(request, 'image.html', ctx)



def process_image(image, max_height, max_width, fish):
    

    fish_id = fish.fish_id
    fish_name = fish.fish_name
    fish_species = fish.fish_species
    weight = fish.weight
    length = fish.length
    lattitude = fish.lattitude
    longitude = fish.longitude
    timestamp = fish.timestamp
    image = np.array(image)
    height = image.shape[1]
    width = image.shape[0]
    ascept_ratio = height/width

    if ascept_ratio < 1:

        new_height = max_height
        new_width = new_height / ascept_ratio
    else:

        new_width = max_width
        new_height = new_width * ascept_ratio

    new_image = cv2.resize(image, (int(new_height), int(new_width)))

    pa = "resized_images/"
    cv2.imwrite("media/"+pa+str(fish_id)+".png",new_image)
    obj = Fish.objects.get(fish_id=fish_id)
    obj.img=str(pa+str(fish_id)+".png")   
   
    obj.save()

    


def getallrecords(request):

    if(request.method=='GET'):
        resp = []
        fishes = Fish.objects.all().order_by("-timestamp")
        
        
        return render(request,'response.html',{"fishes":fishes})

def getallrecordsjson(request):
    if(request.method=='GET'):
        resp = []
        fishes = Fish.objects.all().order_by("-timestamp")
        for fish in fishes:
            print(fish.img)
            pa = "media/resized_images/"+str(fish.fish_id)+".png"
            fish_json = {"fish_id":fish.fish_id,"fish_name":fish.fish_name,"fish_species":fish.fish_species,"weight":fish.weight,"length":fish.length,"lattitude":fish.lattitude,"longitude":fish.longitude,"timestamp":fish.timestamp.strftime('%Y-%m%d %H:%M:%S'),"path":pa}
            resp.append(fish_json)


            data = json.dumps(resp)
            return HttpResponse(data)
        





