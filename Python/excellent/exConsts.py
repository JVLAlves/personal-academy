import os
import string

FILENAME = str(os.environ['HOME']) + '/desktop/excel/pypulation.xlsx'
INSERT_LINE = 3
PAT_COL = 'A'
PAT_ROW = INSERT_LINE + 1
PAT_VAL = 'B'
PAT_TOTAL_COL = 'O'
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