from crypt import methods
from email.policy import default
from flask import Flask, json, request
from bs4 import BeautifulSoup
import requests

api = Flask(__name__)

@api.route('/companhia', methods=['GET'])
def get_companhia():
    data = webscraping()
    response = api.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )    
    return response


def webscraping():
    fundo = request.args.get('fundo', default="", type=str)
    print(fundo)
    site = "https://www.fundsexplorer.com.br/funds/" + fundo
    html = requests.get(site).content
    monta = {}

    dados = BeautifulSoup(html, 'html.parser')
    titulo = dados.find("h1", class_="section-title")
    monta["titulo"] = titulo.text.strip()
    descricoes = dados.find_all('span', class_="description")
    monta["descricao"] = descricoes[0].text.strip()
    monta["dt_constituicao"] = descricoes[1].text.strip()
    monta["cotas"] = descricoes[2].text.strip()
    preco = dados.find("span", class_ = "price")
    monta["preco"] = preco.text.strip()
    indices = dados.find_all("span", class_ = "indicator-value")
    monta["liquidez"] = indices[0].text.strip()
    monta["ult_rendimento"] = indices[1].text.strip()
    monta["dividendo"] = indices[2].text.strip()
    monta["patrimonio"] = indices[3].text.strip()
    monta["valor_patrimonial"] = indices[4].text.strip()
    monta["rentabilidade_mes"] = indices[5].text.strip()
    monta["p_vp"] = indices[6].text.strip()
    return monta
    
if __name__ == '__main__':
    api.run()    