# BEZEN BACKEND ASSIGNMENT

[Hosted Link](https://bezenbkd.azurewebsites.net/)

## Installation
### LIBARRIES USED
- open-cv
- django
- numpy
- sqlite
- json
- request
- python-decouple
- other libraries are listed in requirement.txt


Clone this repository to run in your local machine


### Install libraries

```
pip install -r requirements.txt
```

### Run code
```
cd bezen_backend
python manage.py runserver
```

## routes
1. [addrecord ](https://bezenbkd.azurewebsites.net/addrecord)
A simple HTML page that asks for Fish name , species,weight,length,latitude,longitude and the image and after filling them and clicking on save button a response comes up saying "record added"

2. [schedule](https://bezenbkd.azurewebsites.net/schedule)
This request will start the background process for image resizing and will provide a json response which will contain the fish id and whether it's corresponding image is resized or not

3. [getallrecords]((https://bezenbkd.azurewebsites.net/getallrecords))
An HTML page comes up with a table with columns fish name , fish id, fish species , weight, length,lattitude ,longitude,timestamp and resized img which will contain all the records. Resized img would contain different links and when you click on them you are able to see the resized img

4. [getallrecordsjson]((https://bezenbkd.azurewebsites.net/getallrecordsjson))
This will give you the respinse of all records in json format where img will be replaced by path as image cannot be sent in json therefore image is displayed using HTML page above

SECRET KEY has not been provided so as to follow good practices
