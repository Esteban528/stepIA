from flask import Flask, render_template, request
from chatbot import process_user_input

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    user_input="nombre"
    return render_template('index.html', user_input=user_input)

# Ruta para el procesamiento de la entrada del usuario
@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    response = process_user_input(user_input)
    return render_template('index.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
