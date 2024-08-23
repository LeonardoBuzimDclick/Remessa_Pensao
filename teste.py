from SUBPROGRAMS.parameters import *
from SUBPROGRAMS.functions import *
from clicknium import locator, ui
from clicknium import clicknium as cc
import time
import subprocess
import pyautogui
from datetime import datetime, timedelta
import re
import pygetwindow as gw
import os
import pyperclip
'''
windows = gw.getWindowsWithTitle(title='TOTVS Linha RM - Construção e Projetos  Alias: CorporeRM | 1-OCEANICA ENGENHARIA E CONSULTORIA S.A.')
print(windows)
if windows:
    window=windows[0]
    window.activate()
    window.maximize()

time.sleep(5)
pyautogui.press('down')
print('PRESS BUTTON DOWN')
time.sleep(2)

time.sleep(5)
pyautogui.hotkey('ctrl', 'enter')
print('PRESS BUTTON DOWN')
time.sleep(2)
'''

'''
click_combo = cc.wait_appear(locator.rm.combobox_lancamento, wait_timeout=15)
click_combo.click()
logging.debug('CLICA PARA APARECER CONTA/CAIXA')

select_conta_caixa = cc.wait_appear(locator.rm.listitem_contacaixa, wait_timeout=15)
select_conta_caixa.click()
logging.debug('CLICA PARA APARECER CONTA/CAIXA')

select_conta_caixa = cc.wait_appear(locator.rm.button_contavalor, wait_timeout=15)
select_conta_caixa.click()
logging.debug('CLICA NO BOTÃO [...]')

select_field_search = cc.wait_appear(locator.rm.edit_tbxsearch, wait_timeout=15)
select_field_search.click()
pyautogui.write('%3212')
logging.debug('CLICA NO CAMPO PESQUISA E DIGITA: %3212')

filter_search = cc.wait_appear(locator.rm.button_btnfilter, wait_timeout=15)
filter_search.click()
logging.debug('CLICA NO BOTÃO DO FILTRO')

btn_ok_contacaixa = cc.wait_appear(locator.rm.button_ok_contacaixa, wait_timeout=15)
btn_ok_contacaixa.click()
logging.debug('CLICA NO BOTÃO OK')

btn_executar = cc.wait_appear(locator.rm.button_executar, wait_timeout=15)
btn_executar.click()
logging.debug('CLICA NO BOTÃO EXECUTAR')


avancar_3 = cc.wait_appear(locator.rm.button_remessas_avancar_3, wait_timeout=15)
avancar_3.click()
logging.debug('CLICA EM AVANCAR PARA CONCLUIR')

execute_processo_pagamento = cc.wait_appear(locator.rm.button_exec_processo_pag, wait_timeout=15)
execute_processo_pagamento.double_click()
logging.debug('CLICA EM AVANCAR PARA CONCLUIR')






exec_success_process = waitForImage(image = exec_sucesso, timeout=600, name = 'PRESS BUTTON OK')
if exec_success_process is not None:
    time.sleep(2)
    logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM SUCESSO.')
    time.sleep(2)
    btn_exec_fechar = cc.wait_appear(locator.rm.button_fechar_bordero_autorizacao, wait_timeout=600)
    btn_exec_fechar.click()
    logging.debug('CLICK EM FECHAR.')
    time.sleep(2)


message_erro = cc.wait_appear(locator.rm.edit_textboxlog, wait_timeout=15)
erro_inclusao_bordero = message_erro.get_text()
logging.debug(f'{erro_inclusao_bordero}')
numeros = re.findall(r'1-(\d+)', erro_inclusao_bordero)
ref_lanca = []

for numero in numeros:
    ref_lanca.append(numero)


filter_ref_pag = cc.wait_appear(locator.rm.edit_cod_cliente_fornece, wait_timeout=15)
filter_ref_pag.hover(5)
logging.debug('HOVER FILTER REF PAG')

time.sleep(2)
pyautogui.click(381,308)

time.sleep(2)
pyautogui.press('down')

time.sleep(2)
pyautogui.write('(Personalizar)')

time.sleep(2)
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('Não é igual a')

time.sleep(2)
pyautogui.press('tab')

time.sleep(2)
pyautogui.press('enter')

time.sleep(2)
pyautogui.press('enter')

'''

'''def emailSuccess():
    print(f'{log_path}/{today}/{log_file_name}.log')
    with open(f'{email_path}/emailSuccess.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess
    yag.send(to=str(email_receivers).split(','), subject=f"SUCESSO - BOT REMESSAS FÉRIAS/RESCISÃO",
    contents=htmlSuccess,
    attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Success e-mail sent.')


# wait for image with pyautogui
def waitForImage(image, timeout, name):
    inicialTime = time.time()

    while True:
        # try to find image on screen
        location = pyautogui.locateOnScreen(image=image, confidence=0.9)

        if location is not None:
            # Image found
            logging.info(f'{name} image found.')
            return location

        # checking if timeout is over
        currentTime = time.time()
        if currentTime - inicialTime >= timeout:
            # timeout is over and the image was not found.
            logging.info(f'{name} image not found.')
            return None

        # waiting for searching again
        time.sleep(0.5)


def filter_clean():
    clear_filter_x = waitForImage(image = filter_clear, timeout=30, name = 'FILTER CLEAN')
    if clear_filter_x is not None:
        time.sleep(2)
        pyautogui.click(clear_filter_x)
        logging.debug('CLICA NO BOTÃO X DO LIMPA FILTRO')   
        time.sleep(2)



def obter_intervalo_data():
    hoje = datetime.now()
    dia_semana_hoje = hoje.weekday()  # Retorna um número entre 0 (segunda) e 6 (domingo)

    if dia_semana_hoje in [2, 3, 4]:  # Quarta, quinta ou sexta
        data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
        data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
    elif dia_semana_hoje in [0, 1]:  # Segunda ou terça
        data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
        data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
    else:
        # Lidar com outros dias da semana conforme necessário
        data_inicio = data_fim = None

    return data_inicio, data_fim

def func1():
    # Caminho para a pasta que você deseja explorar
    caminho_pasta = r'X:\\'

    # Certifique-se de substituir o caminho acima pelo caminho real do seu diretório

    # Mude o diretório de trabalho para a pasta desejada
    os.chdir(caminho_pasta)

    # Liste todos os arquivos na pasta
    arquivos = os.listdir(caminho_pasta)

    # Encontre o primeiro arquivo de texto na lista
    primeiro_arquivo_texto = next((arquivo for arquivo in arquivos if arquivo.lower().endswith('.txt')), None)

    if primeiro_arquivo_texto:
        print(f"Nome do primeiro arquivo de texto: {primeiro_arquivo_texto}")
    else:
        print("Nenhum arquivo de texto encontrado na pasta.")


def func():
    # Caminho para a pasta
    caminho_pasta = r'X:\\'

    # Tente mudar para o diretório
    try:
        os.chdir(caminho_pasta)
    except Exception as e:
        print(f'Erro ao tentar acessar o diretório: {e}')
        exit()

    # Liste todos os arquivos na pasta
    arquivos = os.listdir(caminho_pasta)

    # Encontre a última letra usada
    ultima_letra_usada = max([arquivo[-5] for arquivo in arquivos if arquivo.startswith('F15212023') and arquivo.endswith('.txt')], default='A')

    # Determine a próxima letra
    proxima_letra = chr(ord(ultima_letra_usada) + 1)

    print(f'A próxima letra seria: {proxima_letra}')



movimentacao_bancaria()
remessa_pagamento()
encerra_prog()'''



select_filter = cc.wait_appear(locator.rm.select_filter, wait_timeout=60)
select_filter.click()
time.sleep(2)
filter_global = cc.wait_appear(locator.rm.group_filtros_globais, wait_timeout=60)
filter_global.click()
time.sleep(5)
filter_global.set_text('REMESSA PENSAO')