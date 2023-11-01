from flask import Flask, render_template
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/")
def hello_world():

    # Carregando o HTML
    with open('templates\index.html', 'r') as arquivo:
        conteudo = arquivo.read()

    # Criando uma instância do BeautifulSoup
    soup = BeautifulSoup(conteudo, 'html.parser')

    # Inserindo dados nas células
    soup.find(id='celula1').string = 'Dado 5'
    soup.find(id='celula2').string = 'Dado 9'
    soup.find(id='celula3').string = 'Dado 11'

    # Salvando o HTML modificado
    with open('sua_pagina_modificada.html', 'w') as arquivo:
        arquivo.write(str(soup))
    
    return render_template("index.html")