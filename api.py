from flask import Flask, render_template
import urllib2, json

form_site = Flask(__name__)

u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=7V0xcHrzk6S1ZvjjIK4BlQkB6qRQiMgIoVghkgs2")
d = json.loads(u.read())

#print d


@form_site.route('/')
def root():
    return render_template('base.html', title=d['title'], date=d['date'], copyright=d['copyright'], hdurl=d['hdurl'], explanation=d['explanation'])
    
if __name__ == '__main__':
    form_site.debug = True
    form_site.run()

