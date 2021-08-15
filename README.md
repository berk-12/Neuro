# Neuro

## Run
Type ```python app.py``` to run app in Neuro directory.  
Open http://127.0.0.1:5000/ on browser.  
Ready to Go!

## Description
It is the Flask application that returns whether the given address is within Moscow MKAD, if not, its distance from MKAD. It is found by subtracting the radius from the MKAD center coordinates. This app uses Yandex Geocoder API. The Haversine formula was used for the calculations.  
###Useful Links  
https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula  
https://en.wikipedia.org/wiki/Moscow_Ring_Road  
https://en.wikipedia.org/wiki/Module:Location_map/data/Russia_Moscow_MKAD


##Requirements  
  
python==3.8  

blueprint==3.4.2  
certifi==2021.5.30  
charset-normalizer==2.0.4  
click==8.0.1  
colorama==0.4.4  
Flask==2.0.1  
gunicorn==20.1.0  
idna==3.2  
itsdangerous==2.0.1  
Jinja2==3.0.1  
MarkupSafe==2.0.1  
requests==2.26.0  
urllib3==1.26.6  
Werkzeug==2.0.1  
