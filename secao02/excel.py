import xlsxwriter
import os

url = "C:\workspace\Python-RPA\secao02\Dolar e Euro.xlsx"
planilha = xlsxwriter.Workbook(url)
cotacao = planilha.add_worksheet()

#escreve nas células
cotacao.write("A1","Nome")
cotacao.write("B1","Idade")
cotacao.write("A2","Alexandre")
cotacao.write("B2",19)
cotacao.write("A3","Amanda")
cotacao.write("B3",18)

planilha.close()

os.startfile(url)