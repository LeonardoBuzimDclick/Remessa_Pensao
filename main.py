from clicknium import locator, ui
from clicknium import clicknium as cc
from SUBPROGRAMS.functions import *
from SUBPROGRAMS.parameters import *


if __name__ == '__main__':

    sys.excepthook = show_exception_and_exit
    encerrar_processo_windows(nome_processo)
    bot_text_art()
    open_RM()
    loggin_RM()
    enter_coligada()
    check_movimentacao_bancaria()
    enter_contas_a_pagar()
    data_filter()
    desmark_filter()
    result = tabela_vazia()
    if result == True:
        texto_msg = 'SEM REMESSA DE PENSÃO'
        logging.debug(texto_msg)
        emailFinalizado(texto_msg)
        encerra_prog()

    else:
        desbloqueio()
        process_lancamentos()
        proccess_bordero()
        movimentacao_bancaria()
        remessa_pagamento()
        encerra_prog()