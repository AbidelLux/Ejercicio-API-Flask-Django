
from flask import Flask

app = Flask(__name__)
#creando ruta
@app.route('/prueba')
def prueba():
    return "hola a todos soy una api, segunda frase"
if __name__ == '__main__':
    app.run(debug=True,port=4000)

