from django.shortcuts import render, redirect
from .models import QRCode
from ipware import get_client_ip
import requests, json
# Create your views here.

def ip(request):
      client_ip = get_client_ip(request)
      res = requests.get("http://ip-api.com/json/37.110.214.172")
      l_data = res.text
      ldata = json.loads(l_data)
      return ldata     

def index(request):
      a = ip(request)
      print(a)
      
      if request.method == 'POST':
            name = request.POST['name']
            QRCode.objects.create(name=name)
            return redirect('/')

      qrs = QRCode.objects.all().order_by('-id') 



      return render(request, 'index.html', {'qrs':qrs, "data":a})