import os
import exConsts
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from PyQt5.QtWidgets import QMessageBox

def InsertPatient(name, value, workbook):
    sheet = workbook.active
    sheet.insert_rows(exConsts.INSERT_LINE)
    Patref = exConsts.PAT_COL + str(exConsts.PAT_ROW)
    Valref = exConsts.PAT_VAL + str(exConsts.PAT_ROW)
    Totref = exConsts.PAT_TOTAL_COL + str(exConsts.PAT_ROW)
    sheet[Patref] = name
    sheet[Valref] = value
    sheet[Totref] = '=SUM(C{}:N{})'.format(exConsts.PAT_ROW, exConsts.PAT_ROW)

    workbook.save(exConsts.FILENAME)


def GetMonthColumn(month):
    sMonth = month.lower()[:3]
    mlist = exConsts.MONTH_COLS
    for m in mlist:
        if m.startswith(sMonth):
            return mlist[m]['col']


def SearchPatientByName(patname, workbook):
    #Variaveis para Uso interno
    sheet = workbook.active #Planilha
    PatCol = exConsts.PAT_COL #Letra da Coluna do Nome dos Pacientes
    PatRow = exConsts.PAT_ROW #Número da linha dos Pacientes
    cel = PatCol + str(PatRow) #Célula determinada com número e letra
    possibleCels = [] #Possiveis células que combinem com a pesquisa.

    # Busca a célula na planilha com o mesmo nome.
    while sheet[cel].value is not None:
        if sheet[cel].value.startswith(patname.capitalize()):
            cell = {
                "cll": cel,
                "col": PatCol,
                "row": PatRow
            }
            possibleCels.append(cell)
        PatRow += 1
        cel = PatCol + str(PatRow)

    if len(possibleCels) != 0:
        return possibleCels
    #Retentativa mais aberta (as primeiras tres letras da busca
    PatCol = exConsts.PAT_COL
    PatRow = exConsts.PAT_ROW
    cel = PatCol + str(PatRow)
    croppedPat = patname.capitalize()[:3]

    while sheet[cel].value is not None:
        if sheet[cel].value.startswith(croppedPat):
            cell = {
                "cll": cel,
                "col": PatCol,
                "row":PatRow
            }
            possibleCels.append(cell)
        PatRow += 1
        cel = PatCol + str(PatRow)

    return possibleCels

def GetPatientInformation(cell, wb):
    sheet = wb.active
    FirstCell = cell['cll']
    Column = cell['col']
    Row = cell['row']
    PatInfo = []

    ColIn = exConsts.ALPHABET.index(Column)
    NextCol = exConsts.ALPHABET[ColIn+1]
    EndCell = NextCol + str(Row)
    PatRawInfo = sheet[FirstCell:EndCell][0]

    for PRI in PatRawInfo:
        PatInfo.append(PRI.value)

    PatientDict = {
        'Name': PatInfo[0],
        'PayPerSession': PatInfo[1]
    }

    return PatientDict

