
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

@app.route('/delete/<string:name>',methods=['DELETE'])
def delete_character(name):
    if request.method == 'DELETE':
        if name is not None:
            ok =  manager.delete_character(name)
            if ok:
                return jsonify({'ok':ok,'msg':'personaje eliminado'}),200
            else:
                return jsonify({'ok':False,'msg':'no se pudo eliminar'}),404
        return jsonify({'ok': False, 'msg': 'Solicitu incompleta'}), 500
    return jsonify({'msg':'metodo no permitido'}),405

@app.route('/add',methods=['POST'])
def add():
    json = request.get_json()
    manager.add_character(json['name'],json['anime'],json['image'],json['desc'])
    return jsonify({'ok':True,'msg':'personaje agregado con exito'}),200
@app.route('/addVarios',methods=['POST'])
def add_character():
    print(request.data)
    xml = request.data.decode('utf-8')
    root = ET.XML(xml)
    #recorriendo xml
    for element in root:
        #print(element.attrib['name'],element.attrib['anime'])
        #ingresando nuevo elemento
        manager.add_character(element.attrib['name'],element.attrib['anime'],element.attrib['image'],element.text)
    return jsonify({'ok':True,'msg':'todo bien'}),200

@app.route('/showall',methods=['GET'])
def get_character():
    c = manager.get_characters()
    return jsonify(c),200
if __name__ == '__main__':
    app.run(debug=True,port=4000)
