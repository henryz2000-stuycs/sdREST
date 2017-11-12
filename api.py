from flask import Flask, render_template
import urllib2, json

form_site = Flask(__name__)

u_nasa = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=7V0xcHrzk6S1ZvjjIK4BlQkB6qRQiMgIoVghkgs2")
d_nasa = json.loads(u_nasa.read())

u_weather = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?zip=10282,us&APPID=c37f325cc3691cea934b2a6dc1a458a6&units=imperial")
d_weather = json.loads(u_weather.read())

#print d


@form_site.route('/')
def root():
    return render_template('base.html')

@form_site.route('/nasa')
def nasa():
    return render_template('nasa.html', title=d_nasa['title'], date=d_nasa['date'], copyright=d_nasa['copyright'], hdurl=d_nasa['hdurl'], explanation=d_nasa['explanation'])

@form_site.route('/weather')
def weather():
        return render_template('weather.html', name=d_weather['name'], description=d_weather['weather'][0]['description'], temp=d_weather['main']['temp'])
    
if __name__ == '__main__':
    form_site.debug = True
    form_site.run()

