import requests
import json
from flask import render_template
from flask import Flask


app = Flask(__name__)

class client():
 url = "https://solutionsuat.naqelksa.com/WMSAPI/api/values/GetMasterData"

 headers = {"Content-Type": "application/json; charset=utf-8"}

 data = {
     "Username": "Admin",
     "Option": "Masters",
    }
 response = requests.post(url, headers=headers, json=data)
 print("Status Code", response.status_code)
 print("JSON Response ", response.json())
      

root_decorator = app.route('/')
@root_decorator

def index():
    if request.method == 'POST':
     result = request.form
     return render_template('dashboard_with_pivot.html',result=result)