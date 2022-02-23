allowed hosts:  localhost, 127.0.0.1

SECRET KEY has not been provided so as to follow good practices
portno can be any port eg:8000,3000 etc
routes
1. http://127.0.0.1:portno/ or http://127.0.0.1:portno/addrecord 
A simple HTML page that asks for Fish name , species,weight,length,latitude,longitude and the image and after filling them and clicking on save button a response comes up saying "record added"

2. http://127.0.0.1:portno/schedule
This request will start the background process for image resizing and will provide a json response which will contain the fish id and whether it's corresponding image is resized or not

3. http://127.0.0.1:portno/getallrecords
An HTML page comes up with a table with columns fish name , fish id, fish species , weight, length,lattitude ,longitude,timestamp and resized img which will contain all the records. Resized img would contain different links and when you click on them you are able to see the resized img

4.http://127.0.0.1:portno/getallrecordsjson
This will give you the respinse of all records in json format where img will be replaced by path as image cannot be sent in json therefore image is displayed using HTML page above
