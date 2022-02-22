from django.db import connection
from django.shortcuts import redirect, render
from .models import Fish
import json
from django.http import HttpResponse
import requests
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import django.template.loader
from .forms import ImageForm 
import os
from redis import Redis
from rq import Queue
import numpy as np
import cv2

from redis import Redis
from rq import Queue
import threading
# queue = Queue(connection=Redis())
from datetime import datetime
@csrf_exempt
def addrecord(request):

    
    if(request.method=='POST'):
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            print(request.POST)
            newfish = Fish()
            newfish.fish_name = request.POST.get('fish_name')
            newfish.fish_species = request.POST.get('fish_species')
            newfish.weight =request.POST.get('weight')
            newfish.length =request.POST.get('length')
            newfish.lattitude =request.POST.get('lattitude')
            newfish.longitude =request.POST.get('longitude')
            print(request.FILES)
            if len(request.FILES)!=0:
                newfish.img = request.FILES['img']
                print(request.FILES['img'])
            
            newfish.save()
        
        # simp_req = request.body.decode('utf-8')
            # os.system('cmd /k "redis-server"')
            # queue = Queue(connection=Redis())
        # obj = json.loads(simp_req)

        # new_obj = Fish(fish_name = obj['fish_name'],fish_species = obj['fish_species'],weight = obj['weight'],length=obj['length'],lattitude = obj['lattitude'],longitude = obj['longitude'])
        # new_obj.save()
        
        path = "media/images/"+str(request.FILES['img'])

        # for filename in os.listdir(path):
        #     # print(filename, newfish.fish_id)
        #     if filename.find(str(newfish.fish_id)) != -1:
        #         process_image(cv2.imread(os.path.join(path, filename)),  140, 140,  newfish.fish_id)
        #         break
        
        # job = queue.enqueue(process_image, cv2.imread(path),  140, 140,  newfish)
        try:
            process_image(cv2.imread(path),140,140,newfish)
        except Exception:
            t = threading.Thread(process_image, (cv2.imread(path),140,140,newfish))
            t.start()
        return HttpResponse("record added")
    return render(request, './index.html')

        # return HttpResponse("Entry added")


def process_image(image, max_height, max_width, fish):
    print("in process image func")

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
        # image height > image widthimage
        new_height = max_height
        new_width = new_height / ascept_ratio
    else:
        # image height <= image widthimage
        new_width = max_width
        new_height = new_width * ascept_ratio

    new_image = cv2.resize(image, (int(new_height), int(new_width)))

    pa = "resized_images/"
    cv2.imwrite(pa+str(fish_id)+".png",new_image)
    obj = Fish.objects.get(fish_id=fish_id)
    obj.img=str(pa+str(fish_id)+".png")   #  = Fish(fish_id=fish_id,fish_name = fish_name,img=new_image,weight=weight,length=length,lattitude = lattitude,longitude=longitude,timestamp = timestamp)
    print(obj)
    obj.save()

    ## save image to database
    

def store_image_in_db (fist_id):
    pass

def getallrecords(request):

    if(request.method=='GET'):
        resp = []
        fishes = Fish.objects.all().order_by("timestamp")
        # for fish in fishes:
        #     pa = "resized_images/"+str(fish.fish_id)+".png"
        #     fish_json = {"fish_id":fish.fish_id,"fish_name":fish.fish_name,"fish_species":fish.fish_species,"weight":fish.weight,"length":fish.length,"lattitude":fish.lattitude,"longitude":fish.longitude,"timestamp":fish.timestamp.strftime('%Y-%m%d %H:%M:%S'),"path":pa}
        #     resp.append(fish_json)

        #     # getimg(pa+str(fish.fish_id)+".png")
        #     data = json.dumps(resp)
        #     return HttpResponse(data)

        return render(request,'response.html',{"fishes":fishes})


def getimg(path):
    print("reached func")
    return HttpResponse(cv2.imread(path),content_type="image/png")

