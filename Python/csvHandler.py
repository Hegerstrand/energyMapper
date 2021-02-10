import os
import pandas as pd
from openpyxl import load_workbook
import shutil
import os.path
from pathlib import Path

def csv2xl(csvFileName, xlFileName, kommunekode):
    os.listdir('.')

    if not os.path.isfile(xlFileName+".xlsm"):
        print(xlFileName + ".xlsm does not exist in " + str(Path("./").absolute()))
        exit()

    FileName = "../" +xlFileName + str(kommunekode) + ".xlsm"
    print("Writing " + csvFileName + " to " + FileName)
    shutil.copyfile(xlFileName+'.xlsm',  FileName)
    data = pd.read_csv(csvFileName, encoding='latin1', header=0, quotechar='"', delimiter=";")
    book = load_workbook(filename=xlFileName+'.xlsm', read_only=False, keep_vba=True)
    writer = pd.ExcelWriter(FileName, engine='openpyxl')
    writer.book = book
    data.to_excel(writer, sheet_name='BBR')
    writer.save()
    writer.close()
    print("Done writing " + csvFileName + " to " + FileName)

def xl2csv(csvFileName, xlsxFileName, xlsxSheetName):
    os.listdir('..')
    if not os.path.exists("../MapInfo"):
        print("Folder MapInfo not found in parent of " + str(Path().absolute()))
        exit()
    print("Writing " + xlsxFileName + " to " + csvFileName)
    os.listdir("../MapInfo")
    data_xls = pd.read_excel("../" + xlsxFileName, xlsxSheetName, index_col=1, engine='openpyxl')#, encoding='utf-8')
    data_xls.to_csv("../MapInfo/" + csvFileName, encoding='utf-8-sig', header=True, index=False, quotechar='"', sep=";")



