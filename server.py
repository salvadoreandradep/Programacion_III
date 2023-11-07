from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, template_folder='templates')


@app.route('/')
def formulario():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
