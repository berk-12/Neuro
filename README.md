# Address Checker for Moscow MKAD

## Run
To run the project, you need to follow the commands below in root directory;
```
pip install -r requirements.txt
python app.py
``` 
Open [localhost with 5000 port](http://127.0.0.1:5000/) on browser.  
Ready to Go!

## Description
It is the Flask application that returns whether the given address is within Moscow MKAD, if not, its distance from MKAD. It is found by subtracting the radius from the MKAD center coordinates. This app uses Yandex Geocoder API. The Haversine formula was used for the calculations.

### Useful Links  
[Haversine Formula](https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula)  
[Moscow Ring Road](https://en.wikipedia.org/wiki/Moscow_Ring_Road)  
[Russia Moscow MKAD](https://en.wikipedia.org/wiki/Module:Location_map/data/Russia_Moscow_MKAD)


## Tech Stack
This project implemented via Python 3.8.
You may find packages under requirements.txt
