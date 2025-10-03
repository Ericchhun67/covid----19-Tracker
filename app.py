#
# app.py
# Eric Chhun
# 10/1/2025
# Covid Tracker Application
# This program demostrates the main backend script that powers your COVID-19 
# Tracker. It creates the Flask app, fetches live COVID-19 statistics from an 
# external API (like disease.sh or covid19api.com), and routes data to the HTML 
# templates. The root route (/) serves templates/index.html, showing global stats 
# (cases, deaths, recoveries). A second route (/country/<name>) connects to 
# templates/country.html, displaying detailed numbers and charts for a selected 
# country. This backend also links with static/js/charts.js to render interactive 
# charts, and static/css/style.css for styling the UI. Optionally, app.py can 
# save fetched data into data/sample.json for testing without hitting the API 
# repeatedly.



from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
GLOBAL_URL = "https://disease.sh/v3/covid-19/all"
COUNTRY_URL = "https://disease.sh/v3/covid-19/countries/{}"


@app.route('/')
def index():
    """ Home route -> shows Global Covid-19 stats
        Fetches data from API, passes to index.html.
    
    """
    
    try: # handle potential API errors
        response = requests.get(GLOBAL_URL)
        data = response.json()
    except Exception as e:
        print("Error fetching global data", e)
        data = {}
    
    # render index.html, passing global stats
    return render_template('index.html', stats=data)
    
    
    
@app.route('/country', methods=['GET', 'POST'])
def country():
    """ 
        Country route -> shows stats for a user-selected country.
        Renders a form (POST) and fetches data from the API.
    """
    
    country_name = None
    data = {} # default empty data
    
    if request.method == 'POST':
        # get country name from html form
        country_name = request.form.get('country')
        
        try: 
            response = requests.get(COUNTRY_URL.format(country_name))
            stats = response.json()
        except Exception as e:
            print(f"Error fetching data for {country_name}", e)
            
    return render_template('country.html', country=country_name, stats=data)
    

if __name__ == '__main__':
    app.run(debug=True)
        