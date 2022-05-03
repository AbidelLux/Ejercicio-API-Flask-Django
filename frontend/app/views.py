from django.shortcuts import render
import requests
# Create your views here.

endpoint = 'http://127.0.0.1:4000/'
def home(request):
    response = requests.get(endpoint + 'showall')
    characters = response.json()
    context = response.json()
    context = {
        'characters':characters
    }
    return render(request,'index.html',context)