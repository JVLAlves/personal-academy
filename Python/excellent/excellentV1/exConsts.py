import os
import string

FORMAT_CURRENCY_BRL = '"R$" #,##0_);("R$" #,##0)'
BEGINNING_ROW = 2
PATIENT_COLUMN = 'A'
PAT_ROW = BEGINNING_ROW + 1
PAYPERSESSION_COLUMN = 'B'
TOTALPAYMENT_COLUMN = 'O'
MONTH_COLS = {
    'jan': {
        'nome': 'Janeiro',
        'col': 'C'
    },
    'fev': {
        'nome': 'Fevereiro',
        'col': 'D'
    },
    'mar': {
        'nome': 'Março',
        'col': 'E'
    },
    'abr': {
        'nome': 'Abril',
        'col': 'F'
    },
    'mai': {
        'nome': 'Maio',
        'col': 'G'
    },
    'jun': {
        'nome': 'Junho',
        'col': 'H'
    },
    'jul': {
        'nome': 'Julho',
        'col': 'I'
    },
    'ago': {
        'nome': 'Agosto',
        'col': 'J'
    },
    'set': {
        'nome': 'Setembro',
        'col': 'K'
    },
    'out': {
        'nome': 'Outubro',
        'col': 'L'
    },
    'nov': {
        'nome': 'Novembro',
        'col': 'M'
    },
    'dez': {
        'nome': 'Dezembro',
        'col': 'N'
    },

}

def GetMonths():
    months = []
    for m in MONTH_COLS:
        months.append(MONTH_COLS[m]['nome'])
    return months

ALPHABET = list(string.ascii_uppercase)