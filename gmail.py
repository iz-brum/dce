# gmail.py

import smtplib
import email.message
from datetime import date
from prettytable import ALL
from prettytable import PrettyTable
from config import SENDER_EMAIL, SENDER_PASSWORD

def enviar_email(dados):
    # Obter a data atual
    data_atual = date.today().strftime("%d-%m-%Y")
    assunto = f"Relatório de Precipitação {data_atual}"

    corpo_email = f"<h1>Dados de Precipitação {data_atual}</h1><table border='1'><tr><th>Cidade</th><th>Local</th><th>Precipitação (24h)</th></tr>"
    for cidade, local, precipitacao in dados:
        corpo_email += f"<tr><td>{cidade}</td><td>{local}</td><td>{precipitacao}</td></tr>"
    corpo_email += "</table>"

    
    tabela = PrettyTable()
    print(f'\nRELATÓRIO DE PRECIPITAÇÕES ACIMA DE Xmm - data: {data_atual}')
    tabela.field_names = ["Cidade", "Local", "24h (mm)"]
    tabela.hrules = ALL  # Adicionando linhas horizontais

    for cidade, local, precipitacao in dados:
        tabela.add_row([cidade, local, precipitacao])

    print(tabela)

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = SENDER_EMAIL
    msg['To'] = SENDER_EMAIL
    password = SENDER_PASSWORD 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    print(f'\nEnviando e-mail de {msg["From"]} para {msg["To"]}...')
    try:
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        print(f'Conectando ao servidor...')
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado!')
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')
