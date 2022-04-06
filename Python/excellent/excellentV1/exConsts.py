import os
import string

FILENAME = str(os.environ['HOME']) + '/desktop/excel/pypulation.xlsx'
FORMAT_CURRENCY_BRL = '"R$" #,##0_);("R$" #,##0)'
BEGINNING_ROW = 3
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

ALPHABET = list(string.ascii_uppercase)