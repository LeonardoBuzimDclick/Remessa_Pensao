import yagmail
import yaml
import logging
import os
import sys
import pyautogui
from datetime import datetime
from timeit import default_timer as timer
import keyboard

pyautogui.FAILSAFE = False

ref_out = []
base_path = os.getcwd()
log_path = f'{base_path}/LOG'
email_path = f'{base_path}/EMAIL'
image_path = f'{base_path}/IMAGES'
print_path = f'{base_path}/PRINTS'
#user = 'integracao'
user = 'dclick'
password = 'arrobaint;321'
inv = 'INV'
nome_processo = 'RM.exe'
caminho_pasta = r'\\riofs\dados\Documentos Financeiro\Contas a Pagar\Remessas'
caminho_da_pasta_data = r'C:\\Projetos_Remessas\\Remessa_Pix'



with open('config.yaml', 'r', encoding='utf=8') as params:
    config = yaml.safe_load(params)

print(config)

email_login = config['email']['login']
email_password = config['email']['password']
email_receivers = config['email']['receivers']
email_receivers2 = config['email']['receivers_2']
log_level = config['logLevel']


yag = yagmail.SMTP(user=email_login, password=email_password)



# log configs
today = datetime.today().strftime('%d-%m-%Y')
log_file_name = datetime.now().strftime('%H_%M_%S')

if  os.path.exists(f'{log_path}/{today}') == False:
    os.makedirs(f'{log_path}/{today}')

logging.basicConfig(level=log_level, datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s.%(msecs)03dZ;'
                               '%(module)s.%(funcName)s;'
                               '  %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(f'{log_path}/{today}/{log_file_name}.log'), mode='w', encoding='utf-8', delay=False),
                        logging.StreamHandler(sys.stdout)
                    ])

##  IMAGENS  ##
integracao_bancaria = f'{image_path}/integracao_bancaria.PNG'
boleto = f'{image_path}/boleto.PNG'
button_ok = f'{image_path}/button_ok.PNG'
button_ok_2 = f'{image_path}/button_ok_2.PNG'
filter_clear = f'{image_path}/filter_clean.PNG'
lancamentos = f'{image_path}/lancamentos.PNG'
forma_pag = f'{image_path}/forma_pagamento.PNG'
boleto_min = f'{image_path}/boleto_minusculo.PNG'
boleto_min_des = f'{image_path}/boleto_min_desbili.PNG'
exec_sucesso = f'{image_path}/exec_success.PNG'
boleto_min_hab = f'{image_path}/boleto_min_habili.PNG'
table_empty_img = f'{image_path}/table_empty.PNG'
concessionarias_img = f'{image_path}/concessionarias.PNG'
licencas_excedidas = f'{image_path}/licencas_excedidas.PNG'
bordero = f'{image_path}/bordero.PNG'
erro_tempo = f'{image_path}/erro_tempo.PNG'

exe_desbloqueio_sucesso = f'{image_path}/desbloqueio_sucesso.PNG'
tabela_vazia_ferias = f'{image_path}/tabela_vazia_ferias_rescisao.PNG'
exe_desbloqueio_erro = f'{image_path}/desbloqueio_error.PNG'
atualizacao_bordero_excecao = f'{image_path}/atualizacao_bordero_excecao_tratada.PNG'
licencas_2 = f'{image_path}/ERRO 2024_03_26 16_13.PNG'
troca_coligada = f'{image_path}/troca_coligada.PNG'
