import requests
import json
from flask import render_template
from flask import Flask
from .models import getchartdata
from django.shortcuts import render

app = Flask(__name__)

def mainpage(request):

  context={
        "processname": "Receiving performance Per Pallet",
      "warehouseid": 153,
     "Client": 6345210,
     "CheckinID": "CHK-22-00000657",
     "FromDate": "2022-12-13 10:50:34.000",
     "ToDate": "2022-12-13 11:31:58.000"
    } 
 
  return render(request, 'mainpage.html', context)




def getcustomer(request):

  context={
        "processname": "Receiving performance Per Pallet",
      "warehouseid": 153,
     "Client": 6345210,
     "CheckinID": "CHK-22-00000657",
     "FromDate": "2022-12-13 10:50:34.000",
     "ToDate": "2022-12-13 11:31:58.000"
    } 
 
  return render(request, 'mainpage.html', context)





#    url = "https://solutionsuat.naqelksa.com/WMSAPI/api/values/GetMasterData"

#    headers = {"Content-Type": "application/json; charset=utf-8"}

#    data = {
#       "Username": "Admin",
#       "Option": "Masters",
#       }
#    response = requests.post(url, headers=headers, json=data)
  
   
#    return render(request,'mainpage.html')
      

# def getdata(request):
#     assert isinstance(request, HttpRequest)
#     username = request.GET.get('username')
#     Option = request.GET.get('Opton')
   
#     context = {
#         'username': username,
#         'Option': Option,
#     }
#     return render(request, 'mainpage.html', context=context)

# # root_decorator = app.route('/')
# # @root_decorator





# # # import models
# # from models import client
# # # from dejango.shortcuts import render, redirect
# # # from django.utils.translation import gettext as _

# # from models import client

# # def client_list(client):
# #    context = {'client_list': client.objects.all()}
# #    return render(request, "dashboard/client_list.html", context)
# #     # data = serializers.serialize('json', dataset)
# #     # return JsonResponse(data, safe=False)
