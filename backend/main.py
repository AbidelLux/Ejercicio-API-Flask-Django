
from flask import Flask,request
from flask.json import jsonify
from xml.etree import ElementTree as ET
from manage import Manager

app = Flask(__name__)
manager = Manager()
#creando ruta
@app.route('/prueba')
def prueba():
    return "hola a todos soy una api, segunda frase"

@app.route('/add',methods=['POST'])
def add_character():
    print(request.data)
    xml = request.data.decode('utf-8')
    root = ET.XML(xml)
    #recorriendo xml
    for element in root:
        #print(element.attrib['name'],element.attrib['anime'])
        #ingresando nuevo elemento
        manager.add_character(element.attrib['name'],element.attrib['anime'],element.attrib['image'],element.text)
    return jsonify({'msg':'todo bien'}),200

@app.route('/showall',methods=['GET'])
def get_character():
    c = manager.get_characters()
    return jsonify(c),200
if __name__ == '__main__':
    app.run(debug=True,port=4000)
