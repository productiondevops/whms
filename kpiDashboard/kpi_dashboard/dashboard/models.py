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
#  print("Status Code",response.status_code)
#  print("JSON Response ", response.json())
      

# root_decorator = app.route('/')
# @root_decorator
class getchartdata():
  apiurl_ = "https://solutionsuat.naqelksa.com/WMSAPI/Api/values/GetPerformanceperPallet"

  headers = {"Content-Type": "application/json; charset=utf-8"}

  data={

      "processname": "Receiving performance Per Pallet",
      "warehouseid": 153,
     "Client": 6345210,
     "CheckinID": "CHK-22-00000657",
     "FromDate": "2022-12-13 10:50:34.000",
     "ToDate": "2022-12-13 11:31:58.000"
           }
  response = requests.post(apiurl_, headers=headers, json=data)
#   print("Status Code",response.status_code)
#   print("JSON Response ", response.json())   


                                     