import openpyxl
from openpyxl import Workbook, load_workbook
book = load_workbook('try.xlsx', data_only=True)
sheet = book['Conso Broyage 10_35kg']

i = 0 
j = 3     #to average on    #to write the average value of power (p)
p_avrg = 0  #average balue of power
time = 0  

for index , p in enumerate(sheet['E']):
    try:
        p = float(p.value)

        if float(sheet['A' + str(index + 1)].value) >= time + 1:
            sheet['F' + str(j)].value = p_avrg / i
            i = 0
            p_avrg = 0
            j += 1
            time += 1

        p_avrg += p
        i += 1
    except:
        continue

book.save('try.xlsx')