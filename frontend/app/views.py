from django.shortcuts import render
from app.forms import  FileForm
import requests
# Create your views here.

endpoint = 'http://127.0.0.1:4000/'
def home(request):
    context = {
        'characters':[]
    }
    try:

        response = requests.get(endpoint + 'showall')
        characters = response.json()
        context['characters'] = characters
    except:
        print('API no esta levantada')
    return render(request,'index.html',context)

def add(request):
    pass

def delete(request):
    pass

def cargaMasiva(request):
    ctx = {
        'content':None,
        'response':None,
    }
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            print(f.name)
            xml_binary = f.read()
            reponse = requests.post(endpoint + 'addVarios',data=xml_binary)
            if reponse.ok:
                ctx['response'] = 'archivo cargado correcto'
    return render(request,'carga.html',ctx)

