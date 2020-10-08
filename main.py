from flask import Flask, url_for, redirect, render_template, request
import os
import requests


app=Flask(__name__)
app.config['DEBUG']=True


@app.route('/home', methods=['GET', 'POST'])
def home():
    weather_data = []
    if request.method=="POST":
        cityname=request.form['cityname']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'.format(cityname)
        r=requests.get(url).json()
        weather = {
            'city' : cityname,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(weather)
        
    return render_template('home.html',weather_data=weather_data)


if __name__=="__main__":
    app.run()

