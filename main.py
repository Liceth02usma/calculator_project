from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    return jsonify({"response": f"{numero_1} + {numero_2} = {numero_1 + numero_2}"})


@app.route('/restar', methods=['POST'])
def restar():
    data = request.get_json()
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    return jsonify({"response": f"{numero_1} - {numero_2} = {numero_1 - numero_2}"})


@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    data = request.get_json()
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    return jsonify({"response": f"{numero_1} * {numero_2} = {numero_1 * numero_2}"})


@app.route('/division', methods=['POST'])
def division():
    data = request.get_json()
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    return jsonify({"response": f"{numero_1} / {numero_2} = {numero_1 / numero_2}"})


if __name__ == '__main__':
    app.run(debug =True)